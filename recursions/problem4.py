import os 

def traverse_directory_tree(root_path, count):

    # prcoess the current node 
    if os.path.isfile(root_path):
        #store the path
        if root_path.lower().endswith('.py'):
            return 1
        return 0
        #return - return is optional, since yield will automatically handle that when stopiteration is called
    
    if os.path.isdir(root_path):
        total_count = 0
        #recursive call with the childrens
        for child in os.listdir(root_path):
            child_path = os.path.join(root_path, child)
            #yield from - optimized shortcut for calling yield
            total_count += traverse_directory_tree(child_path, count)
        return total_count

root = "D:/DSA"
all_files = []

print("Files found:")
c = traverse_directory_tree(root, 0)
print(c)

#-----------------------------------------------

import os 

def traverse_directory_tree_(root_path):

    # prcoess the current node 
    if os.path.isfile(root_path):
        #store the path
        if root_path.lower().endswith('.py'):
            yield 1
        #return - return is optional, since yield will automatically handle that when stopiteration is called
    
    if os.path.isdir(root_path):
        total_count = 0
        #recursive call with the childrens
        for child in os.listdir(root_path):
            child_path = os.path.join(root_path, child)
            #yield from - optimized shortcut for calling yield
            yield from traverse_directory_tree_(child_path)
        return total_count

root = "D:/DSA"
all_files = []

print("Files found:")
#since yield gives 1 everytime it finds a file, using sum to find total
count = sum(traverse_directory_tree_(root))
print(count)