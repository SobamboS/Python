import calendar
print(calendar.calendar(3045))

from datetime import datetime, timedelta
now = datetime.now()
print(f"{now: %A, %B, %d %Y}")