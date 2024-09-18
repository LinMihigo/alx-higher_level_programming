#!/usr/bin/python3
def roman_to_int(roman_string):
    interpreter = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    int_value = 0
    prev_value = 0
    for char in roman_string:
        current_value = interpreter[char]
        if prev_value < current_value:
            int_value += current_value - 2 * prev_value
        else:
            int_value += current_value
        prev_value = current_value

    return int_value

