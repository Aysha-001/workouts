'''
dfs to traverse the directory tree 

- starting from the root node
- processing the current node
- if the node is a file - save it to an array with full path
- if the node is directory node and not a file
  - recursive call with its children
'''
#problem 3 -

import os

def traverse_directory_tree(root_path, files_list):

    # prcoess the current node 
    if os.path.isfile(root_path):
        #store the path
        files_list.append(os.path.abspath(root_path))
        return 
    
    if os.path.isdir(root_path):
        #recursive call with the childrens
        for child in os.listdir(root_path):
            child_path = os.path.join(root_path, child)
            traverse_directory_tree(child_path, files_list)



#----------------------------------------------------
# USING YIELD

#using 
def traverse_directory_tree_(root_path):

    # prcoess the current node 
    if os.path.isfile(root_path):
        #store the path
        yield os.path.abspath(root_path)
        #return - return is optional, since yield will automatically handle that when stopiteration is called
    
    if os.path.isdir(root_path):
        #recursive call with the childrens
        for child in os.listdir(root_path):
            child_path = os.path.join(root_path, child)
            #yield from - optimized shortcut for calling yield
            yield from traverse_directory_tree_(child_path)

root = "D:/DSA"
all_files = []

print("Files found:")
for f in traverse_directory_tree_(root):
    print(f)