n, l, r = list(map(int, input().split()))
nums = list(map(int, input().split()))

new_list = []
reversed_section = []

for i in range(n):
    if i < l - 1 or i > r - 1:
        new_list.append(nums[i])
    elif i == r - 1:
        reversed_section.append(nums[i])
        reversed_section.reverse()
        new_list.extend(reversed_section)
    else:
        reversed_section.append(nums[i])

for element in new_list:
    print(element, end=' ')