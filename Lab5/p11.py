import re

s = input()

pattern = "[A-Z]"

upper_cases = re.findall(pattern, s)

print(len(upper_cases))