def div_val(x,y):
    try : 
        result = x/y
        print(x)
    except Exception as ex:
        print(f"Somethign Went Wrong as {ex}")
    finally:
        print("All Done!..")

div_val(5,0)