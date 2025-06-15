const btn1 = document.querySelector("#btn1");
const btn2 = document.querySelector("#btn2");
const btn3 = document.querySelector("#btn3");

btn1.onclick = rock;
btn2.onclick = paper;
btn3.onclick = scissors;

let computerMove = "";
let result = "";

function computer() {
  const randomNum = Math.random();
  if (randomNum >= 0 && randomNum < 1 / 3) {
    computerMove = "rock";
  } else if (randomNum >= 1 / 3 && randomNum < 2 / 3) {
    computerMove = "paper";
  } else if (randomNum >= 2 / 3 && randomNum < 1) {
    computerMove = "scissors";
  }
}

function rock() {
  computer();

  if (computerMove === "rock") {
    result = "Tie";
  } else if (computerMove === "paper") {
    result = "You Lose";
  } else if (computerMove === "scissors") {
    result = "You win";
  }
  alert(`You picked Rock and computer picked ${computerMove}. ${result}`);
}

function paper() {
  computer();

  if (computerMove === "rock") {
    result = "You win";
  } else if (computerMove === "paper") {
    result = "Tie";
  } else if (computerMove === "scissors") {
    result = " You Lose";
  }
  alert(`You picked Paper and computer picked ${computerMove}. ${result}`);
}

function scissors() {
  computer();

  if (computerMove === "rock") {
    result = "You Lose";
  } else if (computerMove === "paper") {
    result = "You win";
  } else if (computerMove === "scissors") {
    result = " You Tie";
  }
  alert(`You picked scissors and computer picked ${computerMove}. ${result}`);
}
