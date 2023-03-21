# Subtract a week (7 days)  from a given date.s
from datetime import datetime, timedelta

given_date = datetime(2100, 2, 25)

print(given_date - timedelta(weeks=1))
