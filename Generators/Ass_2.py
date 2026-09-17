# Problem 2
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library. For example:

import random

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)


low = 1
high = 50
n = 20
for val in rand_num(low,high,n):
    print(val)


