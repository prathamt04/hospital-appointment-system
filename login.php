<?php
session_start();

// Database connection
$servername = "localhost";
$username = "root";  // Use your MySQL username
$password = "";  // Use your MySQL password
$dbname = "hospital_booking";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get login data from form
$user = $_POST['username'];
$pass = $_POST['password'];  // Password hashing with md5

// SQL query to check for username and password
$sql = "SELECT * FROM users WHERE username='$user' AND password='$pass'";
$result = $conn->query($sql);

// If a matching user is found
if ($result->num_rows > 0) {
    $_SESSION['username'] = $user;  // Start session and save the username
    header("Location: main.html");  // Redirect to dashboard
} else {
    echo "Invalid username or password";
}

$conn->close();
?>
