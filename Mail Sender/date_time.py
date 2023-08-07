import datetime

now = datetime.datetime.now()

year = now.year
month = now.month
day = now.day

print(year, month, day)

date_of_birth = datetime.datetime(year=2002, month=8, day=29)
print(date_of_birth)

with open("quotes.txt") as file:
    quotes = file.readlines()

print(quotes[0])
