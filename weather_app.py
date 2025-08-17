import requests

api_key="bc7557afd3839100247c0e503425acbf"

user_input = input("Enter City:")



weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric")
if weather_data.status_code != 200:
    print("Error fetching data. Please check the city name.")
else:

    weather=weather_data.json()['weather'][0]['main']
    temp= weather_data.json()['main']['temp']

    print(f"Weather in {user_input}: {weather}")
    print(f"Temperature in {user_input}: {temp}°C")
