import os

def traverse_directory_tree(root, name, level=0):

    
    if os.path.isfile(root):
         print("-" * level, name )

    if os.path.isdir(root):
        print("|" + "-" * level, name +'/')
        for name in os.listdir(root):
            path = os.path.join(root, name)
            
            traverse_directory_tree(path, name,  level + 1)

root = "D:/tmp"


print("Files found:")
traverse_directory_tree(root, root)
  


