# ----------------- Program Task Description
# Write a program that displays a calendar for a specified year and month entered by the user

import datetime
import calendar

year = 2023
month = 3

for i in range(1, 32):
    print(datetime.datetime(year, month, i).strftime("%d %A"))

print(calendar.month(year, month))
