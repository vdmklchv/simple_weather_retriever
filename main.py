import requests
import config

api_key = config.API_KEY

while True:
    city = input("Enter a city. Enter quit to exit: ").lower()
    if city == "quit":
        break
    try:
        response_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric").json()
        if response_data['cod'] == '404':
            print(response_data['message'])
        else:
            print(f"Weather in {city.capitalize()} - {response_data['sys']['country']} now:")
            print(f"Current temperature is {response_data['main']['temp']:.0f} C")
            print(f"Feels like {response_data['main']['feels_like']:.0f} C")
    except TypeError:
        print("Couldn't get weather data from remote server.")
print("Goodbye")
