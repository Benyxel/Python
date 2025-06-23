const btn = document.querySelector("#toggle");

btn.addEventListener("click" ,function () {
    const side = document.querySelector("#sidebar");
    side.classList.toggle("toggle");
    console.log("working")
})