
const url = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=d9029d90403d478c6a48ed328dbb75ad";

fetch(url)
    .then((response) => response.json())
    .then((data)=>{console.log(data.main)})
