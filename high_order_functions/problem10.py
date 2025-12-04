import time
def trace(f):
    def g(x):
        
        start_time = time.time()
        value = f(x)
        
        end_time = time.time()

        duration = end_time - start_time

        print("time taken ", duration, "value ", value)
        return value
        
    return g



def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

fib = trace(fib)
print(fib(3))