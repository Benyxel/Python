
const btn1 = document.querySelector("#btn1")
const btn2 = document.querySelector("#btn2")
const btn3 = document.querySelector("#btn3")

btn1.onclick = rock
btn2.onclick = paper
btn3.onclick = scissors



function rock() {
    let computerMove = ""
    const randomNum = Math.random();
    if (randomNum >= 0 && randomNum < 1 / 3) {
        computerMove = "rock";
    }
    else if (randomNum >= 1 / 3 && randomNum < 2 / 3) {
        computerMove = "paper";
    }

    else if (randomNum >= 2 / 3 && randomNum < 1) {
        computerMove = "scissors";
    }
    alert(computerMove)
}

   

function paper() {
    
}

function scissors() {
    
}