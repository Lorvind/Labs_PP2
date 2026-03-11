import re

s = input()

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,}'

result = re.search(pattern, s)

if result:
    print(result.group())
else:
    print("No email")