import re

s = input()

pattern = "Hello"

result = re.match(pattern, s)

if result:
    print("Yes")
else:
    print("No")