import datetime

def time_count(func):
    start = datetime.datetime.now()
    func()
    stop = datetime.datetime.now()
    diff = stop - start
    print(diff)

def generator():
    gen = [i for i in range(10000000)]
    # print(gen)

time_count(generator)

