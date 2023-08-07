import requests
import datetime


today = datetime.datetime.now()
hour_of_today = today.hour

response = requests.get(url="https://api.sunrise-sunset.org/json?lat=6.695070&lng=-1.615800&formatted=0", verify=False)
response.raise_for_status()

data = response.json()
sunset_hour = data['results']['sunset'].split("T")[1].split("+")[0].split(":")[0]
print(sunset_hour)
