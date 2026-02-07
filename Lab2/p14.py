n = int(input())

nums = list(map(int, input().split()))

frequencies = dict()

for num in nums:
    if num in frequencies:
        frequencies[num] += 1
    else:
        frequencies[num] = 1

max_frequency = max(frequencies.values())

result = []

for key in frequencies.keys():
    if frequencies[key] == max_frequency:
        result.append(key)

result.sort()

print(result[0])