import re

s = input()

pattern = r"\w+"

words = re.findall(pattern, s)

print(len(words))