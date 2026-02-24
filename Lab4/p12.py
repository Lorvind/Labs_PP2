import json

def difference(a: dict, b: dict):

    for key in a:
        if key in b and isinstance(a[key], dict) and isinstance(b[key], dict):
            for dif in difference(a[key], b[key]):
                differences = f"{key}.{dif}"
                yield differences
            
        elif key in b and a[key] != b[key]:
            differences = f"{key} : {json.dumps(a[key], separators=(',',':'))} -> {json.dumps(b[key], separators=(',',':'))}"
            yield differences
        elif key not in b:
            differences = f"{key} : {json.dumps(a[key], separators=(',',':'))} -> <missing>"
            yield differences

    for key in b:
        if key not in a:
            differences = f"{key} : <missing> -> {json.dumps(b[key], separators=(',',':'))}"
            yield differences


a = json.loads(input())
b = json.loads(input())

if a == b:
    print("No differences")
else:
    for dif in difference(a, b):
        print(dif)
