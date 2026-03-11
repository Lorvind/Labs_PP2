s = input()

vowels = "AIUEOaiueo"

if any([True if x in vowels else False for x in s]):
    print("Yes")
else:
    print("No")