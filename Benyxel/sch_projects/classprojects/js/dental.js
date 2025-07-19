const slidebar = document.querySelector("#sidebar");
const toggle = document.querySelector("#toggle-btn");
const close = document.querySelector("#close");

function showToggle() {
  toggle.style.display = "block";
  close.style.display = "none";
}

function showClose() {
  toggle.style.display = "none";
  close.style.display = "block";
}

function resetButtons() {
  toggle.style.display = "";
  close.style.display = "";
  slidebar.classList.remove("toggle");
}

// Toggle sidebar
toggle.addEventListener("click", function () {
  slidebar.classList.toggle("toggle");

  if (slidebar.classList.contains("toggle")) {
    showClose();
  } else {
    showToggle();
  }
});

// Close sidebar
close.addEventListener("click", function () {
  slidebar.classList.remove("toggle");
  showToggle();
});

// Handle screen resize
window.addEventListener("resize", function () {
  if (window.innerWidth >= 997) {
    resetButtons(); // Desktop: let CSS handle visibility
  } else {
    // Mobile: show correct button based on sidebar state
    if (slidebar.classList.contains("toggle")) {
      showClose();
    } else {
      showToggle();
    }
  }
});
