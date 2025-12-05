

import sys

def grep(file_name, word_to_match):

    text = open(file_name).readlines()

    for line in text:
        if word_to_match in line:
            sys.stdout.writelines(line)
    



