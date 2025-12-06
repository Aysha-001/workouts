
def csv_parser(file_name):
    data = open(file_name).read()
    data_p = [line.split(',') for line in data.split('\n')]

    return data_p

print(csv_parser("a.csv"))