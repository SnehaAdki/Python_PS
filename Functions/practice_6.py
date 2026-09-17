
def has_33(arr):
    # approach one
    has_three = False

    for each in arr :
        if each == 3 and has_three == False:
            has_three = True
        elif has_three == True and each == 3:
            return True
        else:
            has_three = False

    return False
    # approach one
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i+1] == 3:
            return True
    return False 


arr = [1,3,3] # True
print(has_33(arr))

arr = [3,1,3] # False
print(has_33(arr))

arr = [1,1,3,3] # False
print(has_33(arr))