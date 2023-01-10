x = [3,4,5]
def abc(x):
    total = 1
    for i in range(1,x+1):
        total *= i
    return total 
print(','.join(map(str,map(abc,x))),end=",")