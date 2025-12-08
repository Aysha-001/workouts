import re
text="         hello  word"

replacement = r"\1-\2"

slugs = re.sub(r"(\w+)\s+(\w+)",replacement,text.strip())

print(slugs)