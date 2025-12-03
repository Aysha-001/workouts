#problem 24

a = [1, 2, 3] 
b = ["a", "b", "c"]

def zipp(a, b):
    return [ (a[i], b[i]) for i in range(len(a)) ]

print(zipp(a, b))

#problem 25

def func(x):
    return x*x
    
def mapp(func, data):
    return [func(x) for x in data]
print(mapp(func, [1,2,3,4]))


#problem 26

def func(x):
    if x%2==0:
        return True
    else:
        return False
    
def filterr(func, data):
    return [x for x in data if func(x) ]
print(filterr(func, [1,2,3,4]))
    

#problem 27

def triplets(n):

    triplets = [(a, b, c) for a in range(n) for b in range(n) for c in range(n) if (a + b) == c]

    return triplets

#problem 28

def enumeratee(arr):
    return [ (i, arr[i]) for i in range(len(arr))]

print(enumeratee([1,2,3,4]))
    
#problem 29

def crd(rows, col):
    return [ ["None"] * col for i in range(rows) ]

print(crd(2,3))


def crd(cols, rows):
    return [ ["None" for j in range(cols)] for i in range(rows) ]

print(crd(2,3))


#problem 32

import string
word = "hello"
test = "helo"
def mutations():
    alphabet = string.ascii_lowercase
    delete = set(word[:i] + word[i+1:] for i in range(len(word)) )
    rotations = set(word[i:] + word[:i] for i in range(len(word)) )
    insert = set(word[:i] + c + word[i+1:] for i in range(len(word)) for c in alphabet)
    
    swapped_letter = set(word[:i] + word[i+1] + word[i] + word[i+2:] 
                         for i in range(len(word) -1 ))
    
    
    comb_set = set.union(delete, rotations, insert, swapped_letter)
    if test in comb_set:
        return True
    else:
        return False