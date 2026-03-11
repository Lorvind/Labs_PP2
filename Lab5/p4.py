import re

s = input()

digits = re.findall(r"\d", s)

if digits:
    print(*digits)
else:
    print()