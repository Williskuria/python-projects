# weather app using api

import requests

key = "eeca9ff99427728bc7478d56f13d2ebe"
city = input("Enter the name of the City: ")

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric",
    verify=False
)

data = response.json()

temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
sea_level = data["main"]["sea_level"]
description = data["weather"][0]["description"]

print(f"City: {city}")
print(f"Temperature: {temp}°C")
print(f"Feels like: {feels_like}°C")
print(f"Humidity: {humidity}%")
print(f"Sea level: {sea_level}")
print(f"Condition: {description}")