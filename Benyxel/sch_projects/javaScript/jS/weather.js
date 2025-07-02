const url = "https://api.openweathermap.org/data/2.5/weather?unit=metric&q=";
const apiKey = "d9029d90403d478c6a48ed328dbb75ad";

weather_fetch();
const search = document.querySelector("#search"),
    searchbtn = document.querySelector("#searchbtn"),
    allcity = document.querySelector("#city"),
  country = document.querySelector("#country"),
  date = document.querySelector("#date")
    

async function weather_fetch(city) {
    
  try {
    const response = await fetch(url + city + `&appid=${apiKey}`);
    const data = await response.json();

    const cityTime = new Date(data.dt * 1000 + (data.timezone * 1000));

      console.log(data);
      allcity.innerHTML = data.name
    country.innerHTML = `(${data.sys.country})`;
    date.innerHTML = cityTime.toLocaleString('en-US', { 
    hour: '2-digit', 
    minute: '2-digit', 
    month: 'short', 
    day: 'numeric' 
});
// Output example: "07:15, Jul 3"
    
      
  } catch (error) {
    console.error(error, "An error occoured");
  }
} 

searchbtn.addEventListener("click", () => {
    weather_fetch(search.value);
   
});
