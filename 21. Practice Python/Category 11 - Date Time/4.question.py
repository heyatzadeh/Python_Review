# Print a date in a the following format

# Day_name  Day_number  Month_name  Year

from datetime import datetime

given_date = datetime(2100, 12, 15)
print(given_date.strftime("%A %d %B %Y"))
