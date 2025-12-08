import re

pattern = r"https?://[a-zA-Z0-9\.-_]+"

text= " go to https://www.google.com and search about re module"

match = re.search(pattern, text)

if match:
    print(match)