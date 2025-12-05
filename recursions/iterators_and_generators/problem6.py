import os 

def traverse_directory_tree_(root_path):

    # prcoess the current node 
    if os.path.isfile(root_path):
        #store the path
        if root_path.lower().endswith('.py'):
            #it will be better to use "with"
            stripped_lines = (line.strip() for line in open(root_path, 'r'))
            line_count = sum(1 for line in stripped_lines if line!= '' and 
                             not line.startswith('#'))
            path = os.path.abspath(root_path)
            yield (line_count, path)
        #return - return is optional, since yield will automatically handle that when stopiteration is called
    
    if os.path.isdir(root_path):
        
        #recursive call with the childrens
        for child in os.listdir(root_path):
            child_path = os.path.join(root_path, child)
            #yield from - optimized shortcut for calling yield
            yield from traverse_directory_tree_(child_path)
        

root = "D:/DSA"


#since yield gives 1 everytime it finds a file, using sum to find total
for data in traverse_directory_tree_(root):
    print(f"number of lines in {data[1]} is {data[0]}")