def cal_uuper_lower(str_val):
    upper = 0
    lower = 0
    for i in str_val:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print(str_val)
    print(f"Number of Uppercase Letter's {upper}")
    print(f"Number of Lowercase Letter's {lower}")

cal_uuper_lower("Hi I am Sneha!..")
