#problem 6

arr=[4,5,6,7]
l = len(arr)
for i in range(l//2):
    arr[i] , arr[(l-i)-1] = arr[l-i-1], arr[i]
print(arr)