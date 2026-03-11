import re

s = input()

p = re.escape(input())

matches = re.findall(p, s)

print(len(matches))