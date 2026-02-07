a = input()
nums = [i**2 for i in list(map(int, input().split()))]
for num in nums:
    print(num, end=' ')