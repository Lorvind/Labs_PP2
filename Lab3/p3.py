def triplet_to_digit(triplet: str):
    conversion_table = {
        "ONE":1,
        "TWO":2,
        "THR":3,
        "FOU":4,
        "FIV":5,
        "SIX":6,
        "SEV":7,
        "EIG":8,
        "NIN":9,
        "ZER":0
    }
    return conversion_table[triplet]

def digit_to_triplet(digit: int):
    conversion_table = {
        1:"ONE",
        2:"TWO",
        3:"THR",
        4:"FOU",
        5:"FIV",
        6:"SIX",
        7:"SEV",
        8:"EIG",
        9:"NIN",
        0:"ZER"
    }
    return conversion_table[digit]

def string_to_num(s: str):
    triplet = ''
    num = 0

    for i in range(len(s)):
        triplet += s[i]
        if (i + 1) % 3 == 0:
            num *= 10
            num += triplet_to_digit(triplet)
            triplet = ''

    return num

def num_to_string(num: int):
    string = ''
    while num > 0:
        string =  digit_to_triplet(num%10) + string
        num //= 10

    return string

def calculate(s: str):
    operations = "+-*"
    left_side = ''
    right_side = ''

    for i in range(len(s)):
        if s[i] in operations:
            left_side = s[:i]
            right_side = s[i + 1:]
            match s[i]:
                case '+':
                    operator = lambda a,b: a+b
                case '-':
                    operator = lambda a,b: a-b
                case '*':
                    operator = lambda a,b: a*b

            break

    left_side = string_to_num(left_side)
    right_side = string_to_num(right_side)
    result = operator(left_side, right_side)
    result = num_to_string(result)

    return result

s = input()
print(calculate(s))