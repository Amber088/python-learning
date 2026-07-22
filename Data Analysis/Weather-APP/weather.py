import requests

city = input("Enter city: ")

# Step 1: City se latitude & longitude nikalo
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

geo_response = requests.get(geo_url)
geo_data = geo_response.json()

# Check karo city mili ya nahi
if "results" not in geo_data:
    print("City not found!")
    exit()

latitude = geo_data["results"][0]["latitude"]
longitude = geo_data["results"][0]["longitude"]

# Step 2: Weather API call
weather_url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

weather_response = requests.get(weather_url)
weather_data = weather_response.json()

current = weather_data["current"]

print("\n------ Weather Report ------")
print("City:", city.title())
print("Temperature:", current["temperature_2m"], "°C")
print("Humidity:", current["relative_humidity_2m"], "%")
print("Wind Speed:", current["wind_speed_10m"], "km/h")