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

document.addEventListener("DOMContentLoaded", function() {
  triggerConfetti();
  var submitButton = document.querySelector("button[type='submit']");

  submitButton.addEventListener("click", function(event) {
    alert("Invalid information detected. Please check your entries.");
});

}, false);