const url = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";
const apiKey = "d9029d90403d478c6a48ed328dbb75ad";

weather_fetch();
const search = document.querySelector("#search"),
  searchbtn = document.querySelector("#searchbtn"),
  allcity = document.querySelector("#city"),
  country = document.querySelector("#country"),
  date = document.querySelector("#date"),
  weatherIcon = document.querySelector("#weather-icon"),
  des = document.querySelector("#des"),
  day = document.querySelector("#day"),
  tem = document.querySelector("#tem"),
  feels = document.querySelector("#feels"),
  low = document.querySelector("#low"),
  high = document.querySelector("#high");

async function weather_fetch(city) {
  try {
    const response = await fetch(url + city + `&appid=${apiKey}`);
    const data = await response.json();
    const cityTime = new Date(data.dt * 1000 + data.timezone * 1000);

    console.log(data);
    allcity.innerHTML = data.name ? data.name : "No city";
    country.innerHTML = `(${data.sys?.country || "N/A"})`;
    date.innerHTML = cityTime.toLocaleString("en-US", {
      hour: "2-digit",
      minute: "2-digit",
      month: "short",
      day: "numeric",
    });
    day.innerHTML = cityTime.toLocaleString("en-US", { weekday: "long" });
    des.innerHTML = data.weather[0].description;
    tem.innerHTML = `${data.main.temp.toFixed(0)}°`;
    feels.innerHTML = `${Math.floor(data.main.feels_like)}°`;
    low.innerHTML = `${Math.floor(data.main.temp_min)}°`;
    high.innerHTML = `${Math.floor(data.main.temp_max)}°`;

    // Output example: "07:15, Jul 3"
    if (data.weather[0].main == "Clouds") {
      weatherIcon.src = "../CSS/assets/images/clouds.png";
    } else if (data.weather[0].main == "Clear") {
      weatherIcon.src = "../CSS/assets/images/clear.png";
    } else if (data.weather[0].main == "Rain") {
      weatherIcon.src = "../CSS/assets/images/rain.png";
    } else if (data.weather[0].main == "Drizzle") {
      weatherIcon.src = "../CSS/assets/images/drizzle.png";
    } else if (data.weather[0].main == "Mist") {
      weatherIcon.src = "../CSS/assets/images/mist.png";
    } else if (data.weather[0].main == "Snow") {
      weatherIcon.src = "../CSS/assets/images/snow.png";
    }
  } catch (error) {
    console.error(error, "An error occoured");
  }
}

searchbtn.addEventListener("click", () => {
  weather_fetch(search.value);
});
