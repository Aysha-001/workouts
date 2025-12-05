import time

def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def trace(f):
    f.level = 0
    def g(x):
        f.level += 1
        if f.level == 1:
            start = time.time()

        value = f(x)

        f.level -= 1
        if f.level == 0:
            end = time.time()
            print("time", end - start)
        return value
    return g

fib = trace(fib)
print(fib(30))