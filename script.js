// Generate a random number between 1 and 100
let secretNumber = Math.floor(Math.random() * 100) + 1;

// Keep track of attempts
let attempts = 0;

// Get elements from the HTML page
const guessInput = document.getElementById("guessInput");
const guessButton = document.getElementById("guessButton");
const message = document.getElementById("message");
const attemptsDisplay = document.getElementById("attempts");
const restartButton = document.getElementById("restartButton");

// When the Guess button is clicked
guessButton.addEventListener("click", function () {

    const guess = Number(guessInput.value);

    // Check if the input is valid
    if (guess < 1 || guess > 100 || guessInput.value === "") {
        message.textContent = "⚠️ Please enter a number between 1 and 100.";
        return;
    }

    // Increase attempts
    attempts++;
    attemptsDisplay.textContent = attempts;

    // Check the guess
    if (guess === secretNumber) {

        message.textContent = "🎉 Correct! You guessed the number!";
        message.style.color = "green";

    } else if (guess < secretNumber) {

        message.textContent = "📈 Too low! Try again.";
        message.style.color = "orange";

    } else {

        message.textContent = "📉 Too high! Try again.";
        message.style.color = "red";
    }

    // Clear the input
    guessInput.value = "";
});

// Restart the game
restartButton.addEventListener("click", function () {

    secretNumber = Math.floor(Math.random() * 100) + 1;
    attempts = 0;

    attemptsDisplay.textContent = attempts;
    message.textContent = "Enter a number to start!";
    message.style.color = "#444";

    guessInput.value = "";
});
