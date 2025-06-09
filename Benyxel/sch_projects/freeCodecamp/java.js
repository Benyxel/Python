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

btn1.onclick = goStore

function goStore() {
    console.log("going to the store");
}

function goCave() {
    console.log("going to the cave");
}

function fightDragon() {
    console.log("Fighting Dragon");
}