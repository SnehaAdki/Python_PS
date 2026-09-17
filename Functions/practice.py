
def letter_for_even(a,b):
    if (a % 2 ==0) and (b % 2 ==0):
        # return a if a<b else b
        return min(a,b)
    else:
        # return a if a>b else b
        return max(a,b)
    
