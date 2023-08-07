import requests
import smtplib
import datetime
import time
'''
fetching the position of ISS in longitude and latitude
'''
SENDER = "amoahalberttest@gmail.com"
PASSWORD = "tissskxcreamrvul"

RECIEVER = "albertamoah2000@gmail.com"
connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=SENDER, password=PASSWORD)


response = requests.get(url="http://api.open-notify.org/iss-now.json")

def is_iss_within_range():
    #getting my location
    MY_LAT = 6.695070
    MY_LONG = -1.615800

    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    #sending myself a mail when the ISS is above my head
    if (iss_longitude - 5 <= MY_LAT <= iss_latitude + 5) and (iss_longitude - 5 <= MY_LONG <= iss_longitude + 5):
        return True

def is_night_time():
    today = datetime.datetime.now()
    hour_of_today = int(today.hour)

    response = requests.get(url="https://api.sunrise-sunset.org/json?lat=6.695070&lng=-1.615800&formatted=0",
                            verify=False)
    response.raise_for_status()

    data = response.json()
    sunset_hour = int(data['results']['sunset'].split("T")[1].split("+")[0].split(":")[0])
    sunrise_hour = int(data['results']['sunrise'].split("T")[1].split("+")[0].split(":")[0])

    if sunrise_hour <= hour_of_today >= sunset_hour:
        return True

while True:
    time.sleep(60)
    if is_night_time() and is_iss_within_range():
         connection.sendmail(from_addr=SENDER, to_addrs=RECIEVER, msg=f"subject: ISS LOCATION\n\n Heyy,\n "
                                                                      f"The ISS is overhead look up")




