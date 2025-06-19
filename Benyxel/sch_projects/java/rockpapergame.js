const ps = require("prompt-sync");
ps()

const prompt = ps({ sigint: true });


let PlayerName = prompt("Enter Your name to Register the Game: ");
function promptcheck(PlayerName) {
    
if (PlayerName =="string") {
    console.log("Enter a valid name");
    }
}

promptcheck(PlayerName)