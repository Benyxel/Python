const btn = document.querySelector("#toggle");
const side = document.querySelector("#sidebar");

// Add toggle class by default to hide sidebar initially
side.classList.add("toggle");

btn.addEventListener("click", function () {
  side.classList.toggle("toggle");
});


function edits() {
  const name = document.querySelector("#name");
const contact = document.querySelector("#contact");
const edit = document.querySelector("#edit");
const isDisabled = !name.disabled
  edit.textContent = isDisabled ? "Edit" : "Save";
    
    name.disabled = !name.disabled;
    contact.disabled = !contact.disabled;

}

const edit = document.querySelector("#edit");

edit.addEventListener("click", edits 

)