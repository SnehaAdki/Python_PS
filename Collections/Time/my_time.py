import time



def function2(n):
    return [r for r in range(0,n)]


def function(n):
    return list(map(str,range(0,n)))

stat_time = time.time()
res = function(1000000)
end_time = time.time()
print(end_time - stat_time)

stat_time = time.time()
res = function2(1000000)
end_time = time.time()
print(end_time - stat_time)

