import re

s = input()

pattern = r"Name: (.+|.+ .+), Age: (\d+)"

pattern_match = re.match(pattern, s)

name = pattern_match.group(1)
age = pattern_match.group(2)

print(name, age)