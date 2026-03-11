def dot_product(a, b):
    result = 0

    for pair in zip(a, b):
        result += pair[0] * pair[1]

    return result

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(dot_product(a, b))
