
def read_reverse(file_name):
    for line in open(file_name).readlines():
        print(line[::-1])

read_reverse("lipsum.txt")