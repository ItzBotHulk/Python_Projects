import requests

api_Key = '8d4a282908d048937f553e59cb7650c8'

user_Input = input("Enter city: ");

weather_Data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_Input}&units=imperial&APPID={api_Key}");

if weather_Data.json()['cod'] == '404':
    print("No City Found");
else:
    weather = weather_Data.json()['weather'][0]['main'];
    temp = round(weather_Data.json()['main']['temp']);

    print(f"The weather in {user_Input} is: {weather}");
    print(f"The temperature in {user_Input} is: {temp}°F");
