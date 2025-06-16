const btn1 = document.querySelector("#btn1");
const btn2 = document.querySelector("#btn2");
const btn3 = document.querySelector("#btn3");

btn1.onclick = rock;
btn2.onclick = paper;
btn3.onclick = scissors;




function computer() {
  let computerMove ="";
  const randomNum = Math.random();
  if (randomNum >= 0 && randomNum < 1 / 3) {
    computerMove = "rock";
  } else if (randomNum >= 1 / 3 && randomNum < 2 / 3) {
    computerMove = "paper";
  } else if (randomNum >= 2 / 3 && randomNum < 1) {
    computerMove = "scissors";
    }
    return "computerMove"
    
}

function playerGame(playerMove) {
    const computerMove = computer();
    let result = "";

    if (playerMove === "scissors") {
     if (computerMove === "rock") {
    result = "Tie";
  } else if (computerMove === "paper") {
    result = "You Lose";
  } else if (computerMove === "scissors") {
    result = "You win";
    
  }
  
}alert(`You picked ${playerMove} and computer picked ${computerMove}. ${result}`);
 
}


 
function rock() {
    computer();
   playerGame("rock")
}
 

function paper() {
  computer();
   playerGame("paper")
  
}

function scissors() {
  computer();
     playerGame("scissors")
 
}
