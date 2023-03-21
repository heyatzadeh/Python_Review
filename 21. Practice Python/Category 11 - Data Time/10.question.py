# Calculate number of days between two given dates
from datetime import datetime, timedelta

date_1 = datetime(2050, 2, 25)

date_2 = datetime(2065, 9, 17)

delta = date_2 - date_1

print(delta.days)
