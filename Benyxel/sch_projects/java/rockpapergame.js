const ps = require("prompt-sync");
ps();

const prompt = ps({ sigint: true });

function playGame(playerMove) {
    function promptcheck() {
  let playerName = prompt("Enter Your name to Register the Game: ");

  // Check if name is empty or contains non-alphabetic characters
  if (
    !playerName ||
    playerName.trim() === "" ||
    !/^[A-Za-z]+$/.test(playerName)
  ) {
    console.log("Please enter a valid name using only letters (A-Z, a-z)!");
    return promptcheck(); // Ask again if name is invalid
  }

  console.log(`Welcome ${playerName}! Let's play Rock, Paper, Scissors!`);
  return playerName;
}
promptcheck();
    
    // starting 
    
}

playGame()

