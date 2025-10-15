const axios = require('axios');

export default async function handler(req, res) {
  console.log('=== PROCESS DONATION API CALLED ===');
  console.log('Method:', req.method);
  console.log('Headers:', req.headers);
  console.log('Body:', req.body);

  // Set CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Handle preflight
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { amount, name, email, phone } = req.body;

    // For testing - use demo response
    console.log('Processing donation for:', name, amount);
    
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Return a test redirect URL
    res.json({
      success: true,
      redirect_url: `/donation-success.html?amount=${amount}&donor=${encodeURIComponent(name)}`,
      message: 'Payment processed successfully (TEST MODE)',
      test: true
    });

  } catch (error) {
    console.error('API Error:', error);
    res.status(500).json({
      success: false,
      error: error.message,
      step: 'Check Vercel logs for details'
    });
  }
}
