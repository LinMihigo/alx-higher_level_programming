#!/usr/bin/python3
def roman_to_int(roman_string):
    int_value = 0
    interpreter = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and interpreter[roman_string[i]] < interpreter[roman_string[i + 1]]:
            int_value -= interpreter[roman_string[i]]
        else:
            int_value += interpreter[roman_string[i]]
    return int_value
