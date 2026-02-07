a = input()
nums = list(map(int, input().split()))

nums.sort(reverse= True)

for num in nums:
    print(num, end=' ')