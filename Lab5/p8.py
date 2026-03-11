import re

s = input()
d = input()

result = re.split(d, s)

print(*result, sep=',')