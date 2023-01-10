import timeit
import time
def long_function():
    print('function start')
    for num in range(2000,3201):
        if num % 7 == 0 and num % 5 != 0:
            print(num, end=",")
    time.sleep(5)
    print('function end')
print(timeit.Timer(long_function).timeit(number=2))