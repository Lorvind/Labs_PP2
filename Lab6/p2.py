n = int(input())

nums = list(filter(lambda x: int(x) % 2 == 0, input().split()))

print(len(nums))