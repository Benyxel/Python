function calculateBMI() {
  // Get user input using prompt
  let weight = prompt("Enter your weight in kg: ");
  let height = prompt("Enter your height in meters: ");

  // Convert strings to numbers
  weight = Number(weight);
  height = Number(height);

  // Calculate BMI
  let bmi = weight / (height * height);

  // Check BMI category
  let category;
  if (bmi < 18.5) {
    category = "Underweight";
  } else if (bmi < 25) {
    category = "Normal weight";
  } else if (bmi < 30) {
    category = "Overweight";
  } else {
    category = "Obese";
  }

  // Show results
  
}

// Run the function
calculateBMI();
