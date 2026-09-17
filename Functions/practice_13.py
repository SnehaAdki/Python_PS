def ran_check(num,low,high):
    # return (num > low and num < high)
    return num in range(low,high+1)


print(ran_check(3,1,10))
print(ran_check(3,3,10))