import re

s = input()

pattern = r"\d{2,}"

pairs = re.findall(pattern, s)

print(*pairs)