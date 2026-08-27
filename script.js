let secretNumber;
let attempts = 0;

const input = document.getElementById("guessInput");
const guessBtn = document.getElementById("guessBtn");
const restartBtn = document.getElementById("restartBtn");
const message = document.getElementById("message");
const attemptsText = document.getElementById("attempts");

function startGame() {
  secretNumber = Math.floor(Math.random() * 100) + 1;
  attempts = 0;
  attemptsText.textContent = attempts;
  message.textContent = "I have chosen a number. Can you guess it?";
  input.value = "";
  input.disabled = false;
  guessBtn.disabled = false;
  input.focus();
}

function makeGuess() {
  const guess = Number(input.value);

  if (!Number.isInteger(guess) || guess < 1 || guess > 100) {
    message.textContent = "⚠️ Please enter a number from 1 to 100.";
    return;
  }

  attempts++;
  attemptsText.textContent = attempts;

  if (guess < secretNumber) {
    message.textContent = "📈 Too low! Try a higher number.";
  } else if (guess > secretNumber) {
    message.textContent = "📉 Too high! Try a lower number.";
  } else {
    message.textContent = `🎉 Correct! You guessed it in ${attempts} attempt${attempts === 1 ? "" : "s"}!`;
    input.disabled = true;
    guessBtn.disabled = true;
  }

  input.select();
}

guessBtn.addEventListener("click", makeGuess);

input.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    makeGuess();
  }
});

restartBtn.addEventListener("click", startGame);

startGame();
