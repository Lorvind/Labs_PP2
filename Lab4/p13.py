import json

def find_all_indexes(key: str):
    indexes = []

    current_index = ""

    validation_num = 0

    start_found = False

    for c in key:
        if c == '[':
            validation_num += 1
            if validation_num > 1:
                return
            start_found = True
        elif c == ']':
            validation_num -= 1
            if validation_num < 0:
                return
            start_found = False
            indexes.append(int(current_index))
            current_index = ""
        elif start_found:
            current_index += c
        else:
            return

    return indexes


def resolve_query(obj: dict, query: str):
    keys = query.split('.')

    temp_obj = obj
    for key in keys:
        if '[' not in key:
            if key not in temp_obj:
                return "NOT_FOUND" 
            temp_obj = temp_obj[key]
        else:
            base_key = key[:key.find('[')]

            if base_key:
                if base_key not in temp_obj or not isinstance(temp_obj[base_key], list):
                    return "NOT_FOUND"
                temp_obj = temp_obj[base_key]
            
            indexes = find_all_indexes(key[key.find('['):])
            if not indexes:
                print(indexes)
                return "NOT_FOUND"
            
            for index in indexes:
                if index < len(temp_obj):
                    temp_obj = temp_obj[index]
                else:
                    return "NOT_FOUND"

    return json.dumps(temp_obj, separators=(',', ':'))


obj = json.loads(input())

n = int(input())

for i in range(n):
    print(resolve_query(obj, input()))