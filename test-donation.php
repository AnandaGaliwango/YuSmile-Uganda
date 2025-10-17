<?php
// test-donation.php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

// Handle preflight requests
if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {
    exit(0);
}

// Get the POST data
$input = json_decode(file_get_contents('php://input'), true);

// Log the received data (for debugging)
error_log("Received donation data: " . print_r($input, true));

// Return a test response
echo json_encode([
    'success' => true,
    'redirect_url' => 'https://www.pesapal.com/demo',
    'message' => 'Test endpoint working! Received: ' . json_encode($input),
    'received_data' => $input
]);
?>
