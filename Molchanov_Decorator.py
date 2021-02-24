from datetime import datetime
from random import randint


def timeit(func):
    def wrapper():
        start = datetime.now()
        result = func()
        stop = datetime.now()
        print(stop - start)
    return wrapper

def decor(func):
    def wrapper(*args):
        print("Start")
        func(*args)
        print("Stop")
    return wrapper


@decor
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    print(l)


@decor
def two(n):
    l = [randint(-5, 5) for i in range(n) if i % 2 == 0]
    print(l)

one(10)
two(10)
