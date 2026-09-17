def spy_game(list_val):
    code = [0,0,7,'x']

    for val in list_val:
        if val == code[0]:
            code.pop(0)
    
    return len(code) == 1


list_val = [1,2,4,0,0,7,5]
print(spy_game(list_val)) # True
 
list_val = [1,0,2,4,0,5,7]
print(spy_game(list_val)) # True 

list_val = [1,7,2,0,4,5,0]
print(spy_game(list_val)) #False