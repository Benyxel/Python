function next() {
  let user = document.querySelector("#username").value;
  if (!user || user.trim() === "") {
    alert("Please enter your name!");
    return false;
  }
  // Save username to localStorage
  localStorage.setItem("userName", user);
  return true;
}

// Check if we're on the BMI page
if (document.querySelector("#username")) {
  // Get username from localStorage
  let savedUser = localStorage.getItem("userName");
  if (savedUser) {
    document.querySelector("#username").innerHTML = "Hi " + savedUser;
  }
}

function BMI() {
  
  let age = document.querySelector("#age").value;
  let height = document.querySelector("#height").value;
  let weight = document.querySelector("#weight").value;
  let savedUser = localStorage.getItem("userName");


  if (!age || !height || !weight) {
    alert("Please fill in all fields!");
    return;
  }

 
  let ageN = parseInt(age);
  let newheight = parseFloat(height) / 100; // Convert cm to meters
  let newweight = parseFloat(weight);

  
  document.querySelector("#ageOP").innerHTML = ageN;
  document.querySelector("#username2").innerHTML = savedUser || "User";
  document.querySelector("#hresult").innerHTML = newheight + " cm";
  document.querySelector("#Wresult").innerHTML = newweight + " kg";

  let bmi = newweight / (newheight * newheight);

  // let category;
  // if (bmi < 18.5) {
  //   category = "Underweight";
  // } else if (bmi >= 18.5 && bmi < 25) {
  //   category = "Normal Weight";
  // } else if (bmi >= 25 && bmi < 30) {
  //   category = "Overweight";
  //   if (category == "Overweight") {
  //     console.log(userName + " " + "You need training🤣😁");
  //   }
  // } else {
  //   category = "Obesity";
  // }

  // console.log(`${userName} your BMI is ${bmi.toFixed(2)}, you're ${category}`);
}
