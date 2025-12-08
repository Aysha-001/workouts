def izip(iterable1, iterable2):
    while True:
        try:
            value1 = next(iterable1)
            value2 = next(iterable2)
        except StopIteration:
            return
        yield(value1, value2)
        
    

a = iter(["a", "b", "c"])
b = iter([1, 2, 3])

for x, y in izip(a, b):
    print(x, y)
    

#izip no longer in python 3
    