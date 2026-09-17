my_list = [1,2,3]
print(my_list)

my_list = [1,2,3,'Sneha']
print(my_list)

print(my_list[:])
print(my_list[-1:])
print(my_list[0:2])
another_lsit = ['x' , 'y']

final = my_list + another_lsit

print(final)

final[0] = 'One'
print(final)

final.append('xxx')
print(final)

final.extend(['zz','qq'])
print(final)

final.append(['qqx','cc'])
print(final)

poped_item = final.pop()
print(final)
print(poped_item)

final.pop(0)
print(final)

n1 = ['x','c','e','a','b']
n1.sort()
print(n1)

n2 = [6,5,8,3,9,1]
n2.sort()
print(n2)

n2.reverse()
print(n2)