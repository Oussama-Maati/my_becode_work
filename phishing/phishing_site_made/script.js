function createConfetti() {
  const confettiContainer = document.createElement('div');
  confettiContainer.classList.add('confetti-container');

  for (let i = 0; i < 100; i++) {
    const confetti = document.createElement('div');
    confetti.classList.add('confetti');
    confetti.style.left = `${Math.random() * 100}%`;
    confetti.style.animationDelay = `${Math.random() * 5}s`;
    confettiContainer.appendChild(confetti);
  }

  document.body.appendChild(confettiContainer);
}

function triggerConfetti() {
  createConfetti();
}

document.addEventListener("DOMContentLoaded", function() {
  triggerConfetti();
  var submitButton = document.querySelector("button[type='submit']");

  submitButton.addEventListener("click", function(event) {
    alert("Invalid information detected. Please check your entries.");
});

}, false);