import datetime



today = datetime.date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)

td = today.ctime()
print(td)

