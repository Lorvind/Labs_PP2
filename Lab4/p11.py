import json

def patch(source: dict, patcher: dict):
    for key in patcher:
        if key in source and isinstance(source[key], dict) and isinstance(patcher[key], dict):
            patch(source[key], patcher[key])
        elif patcher[key] is None:
            source.pop(key, None)
        else:
            source[key] = patcher[key]


source = json.loads(input())
patcher = json.loads(input())

patch(source, patcher)

text = json.dumps(source, separators=(',', ':'), sort_keys=True)
print(text)