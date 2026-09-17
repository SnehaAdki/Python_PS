
from  datetime import date , datetime

my_date = date(2026, 6, 17)

my_date2 = date(2025, 6, 17)

result = my_date-my_date2

print(result)
print(type(result))

print(result.days)

dt_obj = datetime(2022,11,3,22,0)
dt_obj1 = datetime(2021,11,3,22,30)

res = dt_obj - dt_obj1
print(res)
print(type(res))
print(res.days)
print(res.seconds)