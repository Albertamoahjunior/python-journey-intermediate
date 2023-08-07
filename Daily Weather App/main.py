import requests

api_key = "b7cad0cd2012f7cf2b86271670a3b997"
api_url = "https://api.openweathermap.org/data/2.5/onecall"
hour = 0
params ={
    "lat": 6.695070,
    "lon": -1.615800,
    "exclude": "daily,minutely,current",
    "appid": api_key,
}
response = requests.get(url=api_url, params=params)
response.raise_for_status()
data = response.json()["hourly"]

weather_codes = []
while hour < 12:
    weather_id = data[hour]["weather"][0]["id"]
    weather_codes.append(weather_id)
    if weather_id < 700:
        print("print an umbrella")
        break
    hour += 1
