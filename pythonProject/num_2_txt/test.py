def int_to_english(num):
    d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty',
        30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
        70: 'seventy', 80: 'eighty', 90: 'ninety'}
    k = 1000
    m = k * 1000
    b = m * 1000

    assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < k):
        if num % 100 == 0:
            return d[num // 100] + ' hundred'
        else:
            return d[num // 100] + ' hundred and ' + int_to_english(num % 100)

    if (num < m):
        if num % k == 0:
            return int_to_english(num // k) + ' thousand'
        else:
            return int_to_english(num // k) + ' thousand, ' + int_to_english(num % k)

    if (num < b):
        if (num % m) == 0:
            return int_to_english(num // m) + ' million'
        else:
            return int_to_english(num // m) + ' million, ' + int_to_english(num % m)

    if (num % b == 0):
        return int_to_english(num // b) + ' billion'
    else:
        return int_to_english(num // b) + ' billion, ' + int_to_english(num % b)


user_birthYear = input("What's your birth year: ")
year_Const = 2025
print("You're " + str(int_to_english(int(year_Const) - int(user_birthYear))) + " years old.")

