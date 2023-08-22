// Generate a random number between 1 and 100
let randomNumber = Math.floor(Math.random() * 100) + 1;
console.log("randomNumber: ", randomNumber)

let attempts = 0
let lives = 10




//Function that runs on user submit
function checkGuess(event) {
  event.preventDefault();
  let form = event.target;
  let guess = form.guessInput.value;
  let attemptCounter = document.getElementById("attempts")
  let result = "Null"
  lives--;

  if (lives <= 0){
    youLost()
  }
 
  form.guessInput.value = "";
  
  let checkAnswer = validateAnswer(guess);
  attemptCounter.innerText = "Number of attempts: " + attempts;

  
  if (checkAnswer) {

    if (attempts <= 5){
      result = "A"
  }
    else if (attempts <= 7){
      result = "B"
}
    else if (attempts > 7){
      result = "C"
    }
    youWon(result);
  }
}


//play again
function playAgain(){
  location.reload();
  
}

//Function that checks users answer
function validateAnswer(guess) {
  let feedback = document.getElementById("feedback");
  let score = document.getElementById("score");
  attempts ++
  if (guess == randomNumber) {
    return true;
  } else if (guess > randomNumber) {
    feedback.innerText = "Too high! Guess again.";
    return false;
  } else if (guess < randomNumber) {
    feedback.innerText = "Too low! Guess again";
    return false;
  } 
  
  
}

//Function for winner (clear screen (Extra))

function youWon(result) {
  winner = document.getElementById("winnersPage");
  winner.innerHTML =`<h1>YOU WON!</h2>
                   <h2>Well done you guessed correctly</h2>
                   <h2>You're rank is: ${result}</h2>
                   <button id="replay" onclick="playAgain()">Play Again?</button>`;

  winner.style = "transition:3s;x"

  hintDelete = document.getElementById("hintBox")
  hintDelete.innerHTML = "";
}


//Function that gives user a hunt about secret number
function revealHint(){
  attempts++;
  hintText = document.getElementById("hintAnswer");
  if (randomNumber % 2 == 0){
    hintText.innerText = "Secret number is EVEN";

  }
  else{
    hintText.innerText = "Secret number is ODD";

  }
  hintText.style = "font-weight:bold;"
}

//Function if user has had 15 attempts
function youLost(){
  loser = document.getElementById("winnersPage");
  loser.innerHTML = `<h1>YOU LOST</h2>
  <h2>If you haven't guessed by now, you never will...</h2>
  <button id="replay" onclick="playAgain()">Play Again?</button>
  `
  hintDelete = document.getElementById("hintBox")
  hintDelete.innerHTML = "";
}