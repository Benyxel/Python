// let input = document.querySelector("#inp").value;
// console.log(input);
// let btn = document.querySelector("#btn");
// let result = document.querySelector("#result")

// btn.onclick = signup

// function signup() {
//     btn.innerHTML = "Account Created"
//     result.innerHTML = `Your name is ${input}`
// }






function sum() {

const inp = document.querySelector("#fn").value;
const inp2 = document.querySelector("#sn").value;
const btn = document.querySelector("#tt");
const text = document.querySelector("#text");
    
    btn.onclick = sum
    
    const num1 = Number(inp);
    const num2 = Number(inp2);
    let result = num1 + num2;
    text.innerHTML = result
    result 
}
sum()




