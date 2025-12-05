# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from collections import defaultdict
import os 

def extcount(dir_name):
    #files = 
    #for name in list_dir():
    d = defaultdict(int)
    
    for file in os.listdir(dir_name):
        full_path = os.path.join(dir_name, file)
        if os.path.isfile(full_path):
            extension = file.split('.')[-1]
            d[extension] += 1

    for item, value in d.items():
        print(f"{item} - {value}")

root = "D:/DSA"
extcount(root)
        
        