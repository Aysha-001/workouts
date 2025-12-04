
import os 

def split(f, n):
    split = []
    count = 0
    split_num = 0

    with open(f, 'r') as file:
        for line in file:
            split.append(line)
            count+=1

            if count == n:
                output_filename = f"split{split_num}.txt"

                with open(output_filename, 'w') as output:
                    output.writelines(split)

                split_num +=1
                yield os.path.abspath(output_filename)
                count = 0
                split = []
                
for file in split("lipsum.txt", 5):      
    split(file, 6)