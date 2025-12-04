def product(n, m):
    if m==0 or n==0:
        return 0
    if m==1:
        return n
    else:
        return n + product(n, m-1)
        
def calc(n, m):
    abs_n = abs(n)
    abs_m = abs(m)
    
    prod = product(abs_n, abs_m)
    
    if n or m < 0:
        prod *=-1
    
    return prod

print(calc(2,-3))