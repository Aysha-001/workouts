from collections import defaultdict
import os 

def stats(dir_name):
    #files = 
    #for name in list_dir():
    d = defaultdict(dict)
    
    for file in os.listdir(dir_name):
        full_path = os.path.join(dir_name, file)
        if os.path.isfile(full_path):
            stat_info = os.stat(full_path)
            d[file] = {"size" : stat_info.st_size, "m_time": stat_info.st_mtime}

    for item, value in d.items():
        print(f"{item} \t {value['size']} \t {value['m_time']}")

root = "D:/DSA"
stats(root)