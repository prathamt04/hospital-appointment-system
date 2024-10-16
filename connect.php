<?php
	$name = $_POST['name'];
	$contact_no = $_POST['contact_no'];
	$email = $_POST['email'];
	$gender = $_POST['gender'];
	$issue = $_POST['issue'];
	$date = $_POST['date'];

	// Database connection
	$conn = new mysqli('localhost','root','hospital project');
	if($conn->connect_error){
		echo "$conn->connect_error";
		die("Connection Failed : ". $conn->connect_error);
	} else {
		$stmt = $conn->prepare("insert into registration(name, contact_no, email, gender, issue, date) 
		values(?, ?, ?, ?, ?, ?)");
		$stmt->bind_param("sisssi", $name , $contact_no, $email, $gender, $issue, $date);
		$stmt->execute();
		
		$stmt->close();
		$conn->close();
	}
?>