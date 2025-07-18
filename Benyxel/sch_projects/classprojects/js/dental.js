const slidebar = document.querySelector("#sidebar");
const toggle = document.querySelector("#toggle-btn");

// Start with navbar hidden (no toggle class initially)

toggle.addEventListener("click", function () {
  slidebar.classList.toggle("toggle");
  
});

