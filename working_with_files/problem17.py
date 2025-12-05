import sys

def read_reverse(file_name):
    for line in (open(file_name).readlines())[::-1]:
        print(line)

read_reverse("lipsum.txt")


if __name__ == "__main__":
    read_reverse(sys.argv[-1])