def permute(arr):
    if len(arr) <= 1:
        return [arr]
    
    result = []
    for i in range(len(arr)):
        fixed_elem = arr[i]
        rest = arr[:i] + arr[i+1:]
        for res in permute(rest):
            result.append([fixed_elem] + res)
    return result

print(permute([1,2,3]))

'''
the logic used above, i didnt fully came up with them.
thought process - 

take array, run it through each sub array, calling permuate on that, until if its two element swap them
- logic is flawed, as the elements are fixed in place, and doesn't give us all the permutations
---------
- Permutations require each element to be able to occupy every position, not just to swap in place.
- keep one element fixed, and permutate the others.

    - until one element remains

    fix 1 , 
        permutate([2,3])
            fix 2,
                permute([3])
                    returns 3 
                result append 2 + [3] -> [2, 3]
            fix 3,
                permute([2])
                    returns 2
                result append 3 + [2] -> [3, 2]
        result append 1 + [2 , 3]
        result append 1 + [3 , 2]
'''