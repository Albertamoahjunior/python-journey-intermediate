import smtplib
import random
from datetime import datetime
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

with open("quotes.txt") as file:
    quotes = file.readlines()

now = datetime.now()
day = now.day
print(day)

birthdate = datetime(year=2002, month=8, day=29)
albert_birthday = [birthdate, "Albert Amoah Junior"]

SENDER = "amoahalberttest@gmail.com"
PASSWORD = "tissskxcreamrvul"

email_reciever = "albertamoah2000@gmail.com"
connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=SENDER, password=PASSWORD)

#connection.sendmail(from_addr=SENDER, to_addrs=email_reciever, msg=f"subject:{DAYS[day-2]} motivation \n\n Happy {DAYS[day-2]},\n"
#                                                                  f"{random.choice(quotes)}")
'''
Sending emails on the birthday 
'''
if birthdate.month == now.month and birthdate.day == now.day:
    connection.sendmail(from_addr=SENDER, to_addrs=email_reciever, msg=f"subject: Birthday Wishes\n\n Happy Birthday Dear{albert_birthday[1]},\n"
                                                                       f"It is your great day. Enjoy it to the fullest.")
connection.close()
