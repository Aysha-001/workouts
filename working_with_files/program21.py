import sys

def fixed_length_split(file_name, size):
   
    with open(file_name, 'r') as f:
        content = f.read()

    result = []

    for i in range(0, len(content), size):
    
        chunk = content[i:i + size]
        result.append(chunk)

    sys.stdout.write('\n'.join(result))
    
fixed_length_split("lipsum.txt", 10)