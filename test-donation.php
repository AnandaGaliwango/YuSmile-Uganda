<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

// Simple test response
echo json_encode([
    'success' => true,
    'redirect_url' => 'https://demo.pesapal.com/api/redirect',
    'message' => 'Test endpoint working'
]);
?>
