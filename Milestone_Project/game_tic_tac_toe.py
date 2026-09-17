def display(r1,r2,r3):
    print(r1)
    print(r2)
    print(r3)

r1 = [' ',' ',' ']
r2 = [' ',' ',' ']
r3 = [' ',' ',' ']

# display(r1,r2,r3)
# select_value = int(input('Select the input string : '))

def user_choice():

    #initial
    choice = ''
    acceptable_range = range(0,10)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input('Please enter number form (0-10): ')
        if choice.isdigit() == False: 
            print("It's not a. digit!..")
        if choice.isdigit() == True:
            if int(choice) in acceptable_range :
                within_range = True
            else:
                print("Please enter the digit in range form 0 till 10")
                within_range = False

    return int(choice)

def display_game(game_list):
    print("Here is the list!....")
    print(game_list)

def position_choice():
    choice = 'invalid'

    while choice not in ['0','1','2']:
        choice = input("Pick position from (0,1,2): ")
        if choice not in ['0','1','2']:
            # clear_outptu()
            print("Invlaid input please select in range!...")
    return int(choice)

def replacement_choice(game_list,position):
    value = input("Enter the new value: ")
    game_list[position] = value
    return game_list

def gameon_check():
    choice = 'invalid'

    while choice not in ['N' , 'Y']:
        choice = input("Would you like to play ?? Y or N : ")

        if choice not in ['N' , 'Y']:
            print("We didn't understood the input")
        
    if choice == 'Y':
        return True
    return False





gameon = True
game_list = [1,2,3]

while gameon:
    # clear_output()
    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list,position)
    # clear_output()
    display_game(game_list)

    gameon = gameon_check()



