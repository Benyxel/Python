const url =
  "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=d9029d90403d478c6a48ed328dbb75ad";

// fetch(url)
//     .then((response) => response.json())
//     .then((data)=>{console.log(data.main)})

weather_fetch();

async function weather_fetch() {
    try {

        const city = document.querySelector("#city"),
        feels = document.querySelector("#feels"),
            locations = document.querySelector("#locations");
        
        locations.addEventListener("click", function () {
            if (data.cod != "" && data.cod != 200) {
                alert(data.massage);
                return
             }
            // console.log(data.coord.lon, data.coord.lat)
    });
        
    const response = await fetch(url + locations.value);
    if (!response.ok) {
    throw new Error("Could not find the given string");
    }

    const data = await response.json();
    console.log(data);

    
    
   

    city.innerHTML = data.name;
    feels.innerHTML = data.main.feels_like;
    // locations.innerHTML = data;
} catch (error) {
    console.error(error, "An error occured");
}
}
