def reversee(arr):
    
    arr.reverse()
    
    for item in arr:
        if isinstance(item, list):
            reversee(item)
    return arr

print(reversee([[1, 2], [3, [4, 5]], 6]))