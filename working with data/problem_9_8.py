import itertools

#problem 8


#using loops
arr=[1,2,3,4,5]
ans = [0] * len(arr)
s=0
for i in range(len(arr)):
    s += arr[i]
    ans[i] = s
print(ans)

#using itertools
# function returns an iterator , 
# pass it to list, and it exhausts the iterator 

cum_sum = list(itertools.accumulate(arr))
print(cum_sum)

#problem 9

cum_mul = list(itertools.accumulate(arr, func = lambda acc, x: acc * x))
print(cum_mul)