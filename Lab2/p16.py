n = int(input())

nums = list(map(int, input().split()))

unique_nums = set()

for num in nums:
    if num in unique_nums:
        print("NO")
    else:
        print("YES")
        unique_nums.add(num)