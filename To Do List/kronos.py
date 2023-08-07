from datetime import datetime

now = str(datetime.now())
now = now.split(" ")

date = now[0]
time = now[1].split(".")[0]


class Kairos():
    def __init__(self):
        self.time = time
        self.date = date

    def set_kairos(self, time):
        time += ":00"
        self.time = time

    def set_date(self, date):
        self.date = date

class reminder():
    def __init__(self, due_time, due_date):
        self.time = due_time
        self.date = due_date

    def blow_reminder(self, reminder):
        if (self.date == date) and (self.time == time):
            reminder()
