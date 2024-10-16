<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.18.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.18.0/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyDhKjcz5MBIJXZZtlcjG7hb1agDK_VNjpc",
    authDomain: "hosproject-e5781.firebaseapp.com",
    projectId: "hosproject-e5781",
    storageBucket: "hosproject-e5781.appspot.com",
    messagingSenderId: "759779335441",
    appId: "1:759779335441:web:7c1597331832bf8c6600b0",
    measurementId: "G-WYX6JG7W4K"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
</script>

npm install -g firebase-tools
firebase login
firebase init
firebase deploy