import re

pattern = r"\+91\s\d{10}"
pattern2 = r"\+\d{2}\s\d{10}"

phone_number = "+91 1234567890"
match = re.search(pattern2, phone_number)

if match:
    print(match.group(0))
else:
    print("not a valid phone number")