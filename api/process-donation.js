// api/process-donation.js
const fetch = require('node-fetch');

export default async function handler(req, res) {
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Handle preflight request
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { amount, name, email, phone, payment_method } = req.body;

    // Validate required fields
    if (!amount || !name || !email || !phone) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Get environment variables
    const {
      PESAPAL_CONSUMER_KEY,
      PESAPAL_CONSUMER_SECRET,
      PESAPAL_IPN_ID,
      PESAPAL_ENVIRONMENT = 'demo',
      VERCEL_URL
    } = process.env;

    const PESAPAL_API = PESAPAL_ENVIRONMENT === 'demo' 
      ? 'https://cybqa.pesapal.com/pesapalv3'
      : 'https://pay.pesapal.com/v3';

    // Get access token from Pesapal
    const token = await getAccessToken(PESAPAL_API, PESAPAL_CONSUMER_KEY, PESAPAL_CONSUMER_SECRET);
    
    if (!token) {
      throw new Error('Failed to get access token from Pesapal');
    }

    // Create Pesapal order
   const orderData = {
  id: `DON-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
  currency: "UGX",
  amount: amount,
  description: "Donation to YuSmile Uganda",
  callback_url: `${VERCEL_URL ? `https://${VERCEL_URL}` : 'https://yu-smile-uganda.vercel.app'}/donation-success.html`,
  cancellation_url: `${VERCEL_URL ? `https://${VERCEL_URL}` : 'https://yu-smile-uganda.vercel.app'}/donation-cancelled.html`,
  billing_address: {
    email_address: email,
    phone_number: phone,
    first_name: name
  }
};

// Only add notification_id if it exists and is not empty
if (PESAPAL_IPN_ID && PESAPAL_IPN_ID.trim() !== '') {
  orderData.notification_id = PESAPAL_IPN_ID;
}

    const orderResponse = await fetch(`${PESAPAL_API}/api/Transactions/SubmitOrderRequest`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
        'Accept': 'application/json'
      },
      body: JSON.stringify(orderData)
    });

    if (!orderResponse.ok) {
      const errorText = await orderResponse.text();
      throw new Error(`Pesapal API error: ${orderResponse.status} - ${errorText}`);
    }

    const result = await orderResponse.json();
    
    if (result.redirect_url) {
      // Store donation record (you can use a database or serverless database like Vercel Postgres)
      await storeDonationRecord(orderData.id, { name, email, phone, amount });
      
      res.status(200).json({ 
        success: true, 
        redirect_url: result.redirect_url,
        order_id: orderData.id
      });
    } else {
      throw new Error('No redirect URL received from Pesapal');
    }
  } catch (error) {
    console.error('Donation processing error:', error);
    res.status(500).json({ 
      error: 'Donation processing failed',
      message: error.message 
    });
  }
}

async function getAccessToken(apiUrl, consumerKey, consumerSecret) {
  const response = await fetch(`${apiUrl}/api/Auth/RequestToken`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: JSON.stringify({
      consumer_key: consumerKey,
      consumer_secret: consumerSecret
    })
  });
  
  if (response.ok) {
    const data = await response.json();
    return data.token;
  }
  
  return null;
}

async function storeDonationRecord(orderId, donorData) {
  // For now, we'll log to the console
  // In production, connect to a database like Vercel Postgres, MongoDB, etc.
  console.log('Donation record:', {
    orderId,
    ...donorData,
    status: 'pending',
    createdAt: new Date().toISOString()
  });
  
  // Example for Vercel Postgres:
  /*
  const { db } = await import('@vercel/postgres');
  await db.sql`
    INSERT INTO donations (order_id, donor_name, donor_email, donor_phone, amount, status)
    VALUES (${orderId}, ${donorData.name}, ${donorData.email}, ${donorData.phone}, ${donorData.amount}, 'pending')
  `;
  */
}