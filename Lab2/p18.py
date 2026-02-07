n = int(input())

dic = {}

for i in range(1, n + 1):
    s = input()
    if s in dic:
        continue
    else:
        dic[s] = i

sorted_keys = list(dic.keys())
sorted_keys.sort()

for key in sorted_keys:
    print(key, ' ', dic[key])