const slidebar = document.querySelector("#slidebar");
const toggle = document.querySelector("#toggle");

// Start with navbar hidden (no toggle class initially)

toggle.addEventListener("click", function () {
  slidebar.classList.toggle("toggle");
  
});

