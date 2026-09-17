
def blackjack(a,b,c):
    sum_al = a+b+c
    if sum_al <= 21:
        return sum_al
    elif sum_al > 21 and (11 in [a,b,c]):
        return sum_al-10
    else:
        return 'BUST'





print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))