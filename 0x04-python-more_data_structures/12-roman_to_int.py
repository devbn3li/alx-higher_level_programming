#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    numbers = list(map(lambda n: roman_numerals[n], roman_string))
    res_list = []
    res = 0

    for i in range(len(numbers)):
        if numbers[i] <= res:
            res += numbers[i]
        else:
            res = numbers[i] - res
        if i == len(numbers) - 1 or numbers[i + 1] < numbers[i]:
            res_list.append(res)
            res = 0

    return sum(res_list)
