let = 0;
let health = 100;
let gold = 50;
let currentWeaponIndex = 0;
let fighting;
let monsterHealth;
let inventory = ["stick"];

const btn1 = document.querySelector("#btn1");
const btn2 = document.querySelector("#btn2");
const btn3 = document.querySelector("#btn3");
const monsterStats = document.querySelector("#monsterStats");
const monsterName = document.querySelector("#monsterName");
const text = document.querySelector("#text");
const xpText = document.querySelector("#xpText");
const healthText = document.querySelector("#healthText");
const goldText = document.querySelector("#goldText");
const monsterHealthText =document.querySelector("#monsterHealth")

btn1.onclick = goStore;
btn2.onclick = goCave;
btn3.onclick = fightDragon;

function goTown(){
    text.innerText = "You are in the town square. You see a sign that says Store.";
    btn1.innerText = "Go to store";
    btn2.innerText = "Go to cave";
    btn3.innerText = "fightDragon";
    btn1.onclick = goStore;
    btn2.onclick = goCave;
    btn3.onclick = fightDragon;
}

function goStore() {
    text.innerText = "You entered store";
    btn1.innerText = "Buy 10 health (10 gold)";
    btn2.innerText = "Buy weapon (30 gold)";
    btn3.innerText = "Go to town square";
    btn1.onclick = buyHealth;
    btn2.onclick = buyWeapon;
    btn3.onclick = goTown;
  
}

function goCave() {
   
    console.log("going to the cave");
}

function fightDragon() {
    
    console.log("Fighting Dragon");
}

function buyHealth() {};
function buyWeapon() {};