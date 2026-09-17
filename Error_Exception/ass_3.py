# loop using the incorrect input using try, catch, else block & get the square of it


while True:
    try:
        input_val = int(input("Enter a number : "))
        result = input_val ** 2

    except:
        print("An Error Occured!.. Please try again!...")
        continue
    else:
        print(f"Thanks you!... The result is:{result}")
        break

