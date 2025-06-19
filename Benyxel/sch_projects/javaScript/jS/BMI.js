function next() {
  let user = document.querySelector("#username").value;
  user = document.querySelector("#userNames").innerHTML = user;
}
next()






// function BMI() {
 
//   height = parseFloat(height) / 100; // Convert cm to meters
//   weight = parseFloat(weight);

//   let bmi = weight / (height * height);

//   let category;
//   if (bmi < 18.5) {
//     category = "Underweight";
//   } else if (bmi >= 18.5 && bmi < 25) {
//     category = "Normal Weight";
//   } else if (bmi >= 25 && bmi < 30) {
//     category = "Overweight";
//     if (category == "Overweight") {
//       console.log(userName + " " + "You need training🤣😁");
//     }
//   } else {
//     category = "Obesity";
//   }

//   console.log(`${userName} your BMI is ${bmi.toFixed(2)}, you're ${category}`);
// }

// BMI();
