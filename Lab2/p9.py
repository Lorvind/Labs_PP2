a = input()

nums = list(map(int, input().split()))

min_num = min(nums)
max_num = max(nums)

for i in nums:
    if i == max_num:
        print(min_num, end=' ')
    else:
        print(i, end=' ')