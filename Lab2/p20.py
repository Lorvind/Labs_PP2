import sys

n = int(sys.stdin.readline())

dct = {}
out = []

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "set":
        dct[command[1]] = command[2]
    elif command[0] == "get":
        if command[1] in dct:
            out.append(dct[command[1]])
        else:
            out.append(f"KE: no key {command[1]} found in the document")

sys.stdout.write("\n".join(out))