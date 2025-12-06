#if more ; then its probably a c file

from collections import Counter

def check_file(file_name1, filename2):
    content1 = open(file_name1).read()

    content2 = open(filename2).read()



    freq = Counter(content1)
    freq2 = Counter(content2)

    if freq[';'] > freq2[';']:
        print(f"{file_name1} might be a c file")
    else:
        print(f"{file_name1} might be a python file")

check_file('a.py', 'b.c')

    