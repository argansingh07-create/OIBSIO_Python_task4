#WeatherApp
#By-Argan Singh

import requests                                        #request module

api_key = "575dd87613b673598892ac380c3aebd8"            #MyApi_Key

print("____Welcome to Weather App______")
print("Know current Weather of Your City !!")

city = input("Enter Your city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

temperature = data["main"]["temp"]
weather = data["weather"][0]["description"]

print("City:", city)
print("Temperature:", temperature, "°C")
print("Weather:", weather)

print ("Thanks for using this app")