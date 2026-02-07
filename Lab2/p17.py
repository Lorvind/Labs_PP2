n = int(input())

numbers = dict()

for i in range(n):
    number = input()
    if number in numbers:
        numbers[number] += 1
    else:
        numbers[number] = 1

count = 0

for i in numbers.values():
    if i == 3:
        count += 1

print(count)