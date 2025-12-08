import os
import inspect

def document(module):
    for entry in dir(module):
        obj = getattr(module, entry)
      
        if inspect.isfunction(obj):
            #print(obj.__doc__) 
            print(entry + "\n")
            
            print(help(obj))

document(os)