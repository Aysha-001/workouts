import itertools

def my_enumerate(iterable):
    l = range(len(iterable))
    return itertools.izip(iterable, l)


for x, y in itertools.izip(["a", "b", "c"], [1, 2, 3]):
    print(x, y)
    
#--------------
#izip NO LONGER in python 3 , it uses zip


import itertools

def my_enumerate(iterable):
    l = range(len(iterable))
    return zip(iterable, l)


for x, y in my_enumerate([1, 2, 3]):
    print(x, y)

    