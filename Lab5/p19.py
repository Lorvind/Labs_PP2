import re

s = input()

word_pattern = re.compile(r"\b\w+\b")

matches = word_pattern.findall(s)

print(len(matches))