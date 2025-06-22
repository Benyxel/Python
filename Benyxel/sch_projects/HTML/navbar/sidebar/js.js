const toggle = document.querySelector("#toggle")

toggle.addEventListener("click", function () {
    const sdie = document.querySelector("#sidebar")
    sdie.classList.toggle("toggle")
    console.log("working")
})