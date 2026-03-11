import re

s = input()

result = re.match(r"^[A-Za-z].*\d$", s)

if result:
    print("Yes")
else:
    print("No")