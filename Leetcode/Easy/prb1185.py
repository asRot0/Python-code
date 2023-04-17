# importing datetime class
from datetime import datetime

# create datetime
x = datetime(2021, 8, 8)

# display
print("Datetime is :", x)
print(x.strftime('%A'))

# get the date

print("Date is :", x.date())
