import re

s = input()

pattern = r"\b[A-Za-z]{3}\b"

matches = re.findall(pattern, s)

print(len(matches))