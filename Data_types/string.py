
str1 = "Sneha"
print(str1)


str2 = "Sneha's laptop"
print(str2)


str3 = 'Sneha Vijay'
print(str3)

my_val = "Sneha is a Good Gril"
print(my_val)

print(my_val[0:6])
print(my_val[:])
print(my_val[12:])
print(my_val[::-1])
print(my_val[::])

##step size 
print(my_val[::2])
print(my_val[1::2])
print(my_val[1:9:2])


#string concatenation

name = 'Sneha'
last_ltetter = name[2:]

concat_wor = 'Vij'
final = concat_wor + last_ltetter
print(final)


letter = 'z'
print(letter * 10)


x = 'Hellow World'
print(x.upper())
print(x.lower())
print(x.split())
print(x.split('o'))

print('{} very Good Morning!.. Welcome to {}'.format('Sneha',"PS"))

print('The {2} {1} {0}'.format("fox" , 'brown' , 'quick'))
print('The {0} {0} {0}'.format("fox" , 'brown' , 'quick'))

print('The {q} {b} {f}'.format(f="fox" , b='brown' , q='quick'))
print('The {f} {f} {f}'.format(f="fox" , b='brown' , q='quick'))