import re

s = input()

digits_pattern = re.compile(r"\d+$")

if digits_pattern.match(s):
    print("Match")
else:
    print("No match")