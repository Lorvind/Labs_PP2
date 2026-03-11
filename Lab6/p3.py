n = int(input())

words = input().split()
indexes = enumerate(words, start=0)

for index, word in indexes:
    print(f"{index}:{word}", end=' ')