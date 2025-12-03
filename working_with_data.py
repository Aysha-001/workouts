#problem 12

arr = [1,2,3,4,5,6,7,8]
k=[]
l = len(arr)

split_size = 3

for i in range(0, l, split_size):
    
        
    k.append(arr[i : i + split_size ])
    
print(k)


#list comprehension

sp = [ arr[i : i + split_size] for i in range(0, l, split_size)]
print(sp)


#problem 13

arr = ['python', 'perl', 'java', 'c', 'haskell', 'ruby']
def lensort(arr):
    arr.sort(key=lambda x: len(x))

lensort(arr)
print(arr)

#problem 16

arr = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']

arr.sort(key = lambda x : x.split('.')[1])
print(arr)

