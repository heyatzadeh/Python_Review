# Add a week (7 days) and 12 hours to a given date

from datetime import datetime, timedelta

given_date = datetime(2050, 3, 15, 10, 0, 0)

print(given_date + timedelta(weeks=1, hours=12))
