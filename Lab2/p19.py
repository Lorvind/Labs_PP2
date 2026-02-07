n = int(input())

dic = {}

for _ in range(n):
    name, count = list(input().split())
    count = int(count)

    if name in dic:
        dic[name] += count
    else:
        dic[name] = count

sorted_keys = list(dic.keys())
sorted_keys.sort()

for key in sorted_keys:
    print(key, ' ', dic[key])