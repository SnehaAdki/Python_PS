

from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


def play_guess():
    guess = None
    while guess not in ['0','1','2']:
        guess=input("Pick a number 0 , 1, 2: ")

    return int(guess)



def gacheck_guess(shuffle_list_val , my_index):
    print(shuffle_list_val)
    if shuffle_list_val[my_index] == 'O' :
        return "Correct Guess"
    return "Wrong Guess"


my_list = ['','O','']
shuffle_list_val =   shuffle_list(my_list)  

my_index = play_guess()

print(gacheck_guess(shuffle_list_val,my_index))



