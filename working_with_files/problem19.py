import sys

def getlines(file_name):
    return open(file_name).readlines()

def head(file_name):
    text = getlines(file_name)
    sys.stdout.writelines(text[:10])
       

def tail(file_name):
    text = getlines(file_name)
    sys.stdout.writelines(text[-10:])


tail("lipsum.txt")