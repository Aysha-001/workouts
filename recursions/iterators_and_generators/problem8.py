import itertools

def peep(iterator):
    
    first_elem = next(iterator)
    
    return itertools.chain([first_elem], iterator)
    
res = peep(iter([1,2,3]))

for r in res:
    print(r)