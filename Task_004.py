""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. """


def code_string(text_str: str):
    count = 1
    res = ''
    for i in range(len(text_str)-1):
        if text_str[i] == text_str[i+1]:
            count += 1
        else:
            res += str(count) + text_str[i]
            count = 1
    if count > 1 or (text_str[len(text_str)-2] != text_str[-1]):
        res += str(count) + text_str[-1]
    return res


def decode_string(text_str: str):
    number = ''
    res = ''
    for i in range(len(text_str)):
        if not text_str[i].isalpha():
            number += text_str[i]
        else:
            res += text_str[i] * int(number)
            number = ''
    return res


my_str = ''
with open('origin.txt', 'r') as f:
    my_str = f.read()

with open('code.txt', 'w') as f:
    f.write(code_string(my_str))

with open('code.txt', 'r') as f:
    my_str2 = f.read()

with open('decode.txt', 'w') as f:
    f.write(decode_string(my_str2))
