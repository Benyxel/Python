// let name_1 = "Kofi";
// let age_1 = 26
// let name_2 = "Kwame" ;
// let age_2 = 48

// if (age_1 > age_2) {
//     console.log(`${name_1} is older than ${name_2}`)
// }

// else {
//     console.log(`${name_2} is older than ${name_1}`)
// }

// age_1 > age_2 ? console.log(`${name_1} is older than ${name_2}`) : console.log(`${name_2} is older than ${name_1}`)

// let data = ["Kwame", "Kofi", 43, 57, "Maame", "Abena", 45, 100]

// for (let x of data){
//     let ls = String(x);
//     let als = ls.toLowerCase()
//     if( als == "kofi"){
//         console.log(x)
//     }

// }

// for (let x of data){
//     if (typeof x == "string" && x.toLowerCase() == "kofi")
//     console.log( `${typeof x} + ${x}`)
// }

// for (let x of data){
//     console.log(x)
// }

const ps = require("prompt-sync");
ps();
const prompt = ps({ sigint: true });

let grade = prompt("Enter your grade: ");
grade = parseInt(grade); 

function checkResult(grade) {
  if (isNaN(grade)) {
    return "Please enter a valid number";
  }

  if (grade >= 50) {
    return "Pass";
  } else {
    return "Fail";
  }
}

let result = checkResult(grade);
console.log(`Your grade is ${grade} and you ${result}`);
