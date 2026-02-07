n = int(input())
elements = list(map(int, input().split()))
q = int(input())

for i in range(q):
    command = input().split()
    operation = command[0]
    if len(command) > 1:
        x = int(command[1])

    match operation:
        case "abs":
            func = lambda a: a if a > 0 else -a
        case "add":
            func = lambda a: a + x
        case "multiply":
            func = lambda a: a * x
        case "power":
            func = lambda a: a ** x

    for i in range(len(elements)):
        elements[i] = func(elements[i])


for element in elements:
    print(element, end=' ')