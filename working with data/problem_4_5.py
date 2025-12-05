#products using reduce and lambda

#problem 4
from functools import reduce


#product function
def product(arr):
    p = 1
    for n in arr:
        p *= n
    return p

#problem 5
def fact(n):
    return product(range(1, n+1))


#using reduce
listo = [1,2,3,4,5]
products = reduce(lambda x, y: x * y, listo)
print(products)