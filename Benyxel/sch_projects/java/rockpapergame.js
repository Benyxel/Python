const btn1 = document.querySelector("#btn1");
const btn2 = document.querySelector("#btn2");
const btn3 = document.querySelector("#btn3");

btn1.onclick = rock;
btn2.onclick = paper;
btn3.onclick = scissors;

let computerMove = "";

function computer() {

  const randomNumber = Math.random();
  
  if (randomNumber >= 0 && randomNumber < 1 / 3) {
    computerMove = "rock";
  } else if (randomNumber >= 1 / 3 && randomNumber < 2 / 3) {
    computerMove = "paper";
  } else if (randomNumber >= 2 / 3 && randomNumber < 1) {
    computerMove = "scissors";
  }
  console.log(computerMove);
}

function playerMove() {
  let result = ""
  if (computerMove === "rock") {
    result = "Tie";
  }
  else if (computerMove === "paper") {
    result = ""
  }
}


function rock() {
  computer();
}

function paper() {
  computer();
}

function scissors() {
  computer();
}
