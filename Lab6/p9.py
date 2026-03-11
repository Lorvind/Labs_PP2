n = int(input())

keys = input().split()
values = input().split()

dic = {}

for key, value in zip(keys, values):
    dic[key] = value

query = input()

if query in dic:
    print(dic[query])
else:
    print("Not found")