import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=%t+%C"

response = requests.get(url)

print("\n🌤 Current Weather")
print("City:", city)
print("Weather:", response.text)