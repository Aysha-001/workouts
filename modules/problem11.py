
import zipfile
import sys


def zipping(name_of_zip, files ):
    with zipfile.ZipFile(name_of_zip, 'w') as zf:
        for file in files:
            zf.write(file)

if __name__ == "__main__":
    name_of_zip = sys.argv[1]
    files = sys.argv[2:]
    print(name_of_zip, files)
    zipping(name_of_zip, files)