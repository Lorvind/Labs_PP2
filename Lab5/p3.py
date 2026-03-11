import re

s = input()

p = input()

count = len(re.findall(p, s))

print(count)