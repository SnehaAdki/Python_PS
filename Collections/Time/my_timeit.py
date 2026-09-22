import timeit

stmt= '''
function(100)
'''
setup = '''
def function(n):
    return list(map(str,range(0,n)))
'''

val =  timeit.timeit(stmt,setup,number=1000000)
print(val)


stmt2= '''
function2(100)
'''
setup2 = '''
def function2(n):
    return [r for r in range(0,n)]
'''

val =  timeit.timeit(stmt = stmt2,setup= setup2,number=1000000)
print(val)