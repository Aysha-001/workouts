def square(x): return len(x)

def vectorize(f):
    f.result = []
    def wrap(arr):
        for item in arr:
            f.result.append(f(item))
        
        return f.result
    return wrap

f = vectorize(square)
print(f(["hello", "world"]))
    