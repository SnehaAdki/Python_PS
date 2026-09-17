from datetime import datetime

datetime_object = datetime.now()
print(datetime_object)

# datetime(year,month,day,hour,minute,second)
my_dob = datetime(1997,6,17,4,55,50)
print(my_dob)

my_dob = my_dob.replace(year=1998,month=7,day=18,hour=5,minute=56,second=51)
print(my_dob)

