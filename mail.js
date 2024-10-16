document.getElementById('contactForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent default form submission

  const formData = new FormData(this);

  fetch('save.php', {
      method: 'POST',
      body: formData
  })
  .then(response => response.text())
  .then(data => {
      // Show success message
      const alertDiv = document.querySelector('.alert');
      alertDiv.style.display = 'block';
      alertDiv.textContent = data; // Display the response from save.php
  })
  .catch(error => console.error('Error:', error));
});
