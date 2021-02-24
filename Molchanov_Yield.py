def gen_countdown(n):
    while n != 0:
        yield n - 1
        n -= 1

g = gen_countdown(4)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(type(g))
print(iter(g))


# get from https://www.youtube.com/watch?v=ZjaVrzOkpZk