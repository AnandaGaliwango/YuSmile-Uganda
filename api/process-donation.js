// api/process-donation.js
const axios = require('axios');

module.exports = async (req, res) => {
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Handle preflight request
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // Only allow POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { amount, name, email, phone, payment_method } = req.body;

    console.log('Processing donation:', { amount, name, email, phone });

    // For now, return a test response
    // Replace this with actual Pesapal integration later
    const testRedirectUrl = `https://cybqa.pesapal.com/pesapalv3/api/RedirectToMobile/ProcessPayment?amount=${amount}&currency=UGX&description=Donation+to+YuSmile+Uganda&email=${encodeURIComponent(email)}&phone=${phone}&name=${encodeURIComponent(name)}`;

    res.status(200).json({
      success: true,
      redirect_url: `/donation-success.html?amount=${amount}&donor=${encodeURIComponent(name)}`,
      message: 'Payment processing initiated',
      test_mode: true
    });

  } catch (error) {
    console.error('Error in process-donation:', error);
    
    res.status(500).json({
      success: false,
      error: 'Internal server error',
      message: error.message
    });
  }
};
