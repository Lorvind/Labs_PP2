import re

s = input()

found = re.findall("cat|dog", s)

if found:
    print("Yes")
else:
    print("No")