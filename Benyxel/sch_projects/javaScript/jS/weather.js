const url =
  "https://api.openweathermap.org/data/2.5/weather?unit=metric&q=";

const apiKey = "d9029d90403d478c6a48ed328dbb75ad"

weather_fetch();
const search = document.querySelector("#search"),
searchbtn = document.querySelector("#searchbtn");


async function weather_fetch(city) {
    try {
    const response = await fetch(url + city + `&appid=${apiKey}`);
        const data = await response.json();
        console.log(data)
} 
    catch (error) {
    console.error(error,"An error occoured")
}  
    
   
}

searchbtn.addEventListener("click", () => {
    weather_fetch(search.value);
} )
