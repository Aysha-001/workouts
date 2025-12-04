#problem 2
def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def check_len(lines):
    return (line for line in lines if len(line)>40)

def printlines(lines):
    for line in lines:
        print(line, end="")

def main(filenames):
    lines = readfiles(filenames)
    lines = check_len(lines)
    printlines(lines)

main(["lipsum.txt"])