<?php
// Database configuration
$host = 'localhost'; // Change this if your database server is different
$db = 'medcare_db';  // Your database name
$user = 'root';      // Your database username
$pass = '';          // Your database password

// Create connection
$conn = new mysqli($host, $user, $pass, $db);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $name = $conn->real_escape_string($_POST['name']);
    $pnum = $conn->real_escape_string($_POST['pnum']);
    $email = $conn->real_escape_string($_POST['email']);
    $gender = $conn->real_escape_string($_POST['gen']);
    $issue = $conn->real_escape_string($_POST['issue']);
    $appointment_date = $conn->real_escape_string($_POST['Date']);
    $doctor = $conn->real_escape_string($_POST['doctors']);

    // Insert data into the database
    $sql = "INSERT INTO appointments (name, pnum, email, gen, issue, Date, doctors) 
            VALUES ('$name', '$pnum', '$email', '$gender', '$issue', '$appointment_date', '$doctor')";

    if ($conn->query($sql) === TRUE) {
        echo "Appointment booked successfully!";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Close the connection
$conn->close();
?>
