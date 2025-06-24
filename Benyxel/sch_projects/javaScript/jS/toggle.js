const btn = document.querySelector("#toggle");
const side = document.querySelector("#sidebar");

// Add toggle class by default to hide sidebar initially
side.classList.add("toggle");

btn.addEventListener("click", function () {
  side.classList.toggle("toggle");
});
