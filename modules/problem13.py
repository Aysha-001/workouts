#example code in the site have errors

#tablib, seem to be changed, encountered errors

import tablib


def set_data(csv_content):
    data = tablib.Dataset() 
    #for i, line in enumerate(csv_content.split("\n")):
    #    data.append([line, i])
    data.csv = csv_content
    return data
    

def convert(csvfile, excel_name):
    csv_content = open(csvfile,"r").read()

    data = set_data(csv_content)

    with open(excel_name, 'wb') as f:
        #f.write(data.xls)
        #f.write(data.export('xls'))
        pass


convert("a.csv","a.xls")
