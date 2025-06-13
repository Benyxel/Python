const ps = require("prompt-sync");

ps();

const prompt = ps({sigint : true});

let userName = prompt("Hello Enter Your name: ");
console.log(`Welcome ${userName}`);

