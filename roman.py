from sys import argv
import re


def to(num):
    num = int(num)

    m = num // 1000 * 'M'
    num %= 1000
    cm = num // 900 * 'CM'
    num %= 900
    d = num // 500 * 'D'
    num %= 500
    cd = num // 400 * 'CD'
    num %= 400
    c = num // 100 * 'C'
    num %= 100
    xc = num // 90 * 'XC'
    num %= 90
    L = num // 50 * 'L'
    num %= 50
    xL = num // 40 * 'XL'
    num %= 40
    x = num // 10 * 'X'
    num %= 10
    ix = num // 9 * 'IX'
    num %= 9
    v = num // 5 * 'V'
    num %= 5
    iv = num // 4 * 'IV'
    num %= 4
    i = num * 'I'

    print(m + cm + d + cd + c + xc + L + xL + x + ix + v + iv + i)


def frm(roman):
    roman = roman.upper()
    total = 0
    while roman.startswith('M'):
        total += 1000
        roman = roman[1:]
    while roman.startswith('CM'):
        total += 900
        roman = roman[2:]
    while roman.startswith('D'):
        total += 500
        roman = roman[1:]
    while roman.startswith('CD'):
        total += 400
        roman = roman[2:]
    while roman.startswith('C'):
        total += 100
        roman = roman[1:]
    while roman.startswith('XC'):
        total += 90
        roman = roman[2:]
    while roman.startswith('L'):
        total += 50
        roman = roman[1:]
    while roman.startswith('XL'):
        total += 40
        roman = roman[2:]
    while roman.startswith('X'):
        total += 10
        roman = roman[1:]
    while roman.startswith('IX'):
        total += 9
        roman = roman[2:]
    while roman.startswith('V'):
        total += 5
        roman = roman[1:]
    while roman.startswith('IV'):
        total += 4
        roman = roman[2:]
    while roman.startswith('I'):
        total += 1
        roman = roman[1:]

    print(total)


def tojk(num):
    num = int(num)

    m = num // 1000 * 'M'
    num %= 1000
    cm = num // 900 * 'CM'
    num %= 900
    d = num // 500 * 'D'
    num %= 500
    cd = num // 400 * 'CD'
    num %= 400
    c = num // 100 * 'C'
    num %= 100
    xc = num // 90 * 'XC'
    num %= 90
    L = num // 50 * 'L'
    num %= 50
    xL = num // 40 * 'XL'
    num %= 40
    x = num // 10 * 'X'
    num %= 10
    ix = num // 9 * 'IX'
    num %= 9
    v = num // 5 * 'V'
    num %= 5
    iv = num // 4 * 'IV'
    num %= 4
    i = num * 'I'

    roman = m + cm + d + cd + c + xc + L + xL + x + ix + v + iv + i
    roman = re.sub('M', '1000', roman)
    roman = re.sub('D', '500', roman)
    roman = re.sub('C', '100', roman)
    roman = re.sub('L', '50', roman)
    roman = re.sub('X', '10', roman)
    roman = re.sub('V', '5', roman)
    roman = re.sub('I', '1', roman)

    print(roman)


def frmjk(roman):
    roman = str(roman)
    total = 0
    while roman.startswith('1000'):
        total += 1000
        roman = roman[4:]
    while roman.startswith('1001000'):
        total += 900
        roman = roman[7:]
    while roman.startswith('500'):
        total += 500
        roman = roman[3:]
    while roman.startswith('100500'):
        total += 400
        roman = roman[6:]
    while roman.startswith('100'):
        total += 100
        roman = roman[3:]
    while roman.startswith('10100'):
        total += 90
        roman = roman[5:]
    while roman.startswith('50'):
        total += 50
        roman = roman[2:]
    while roman.startswith('1050'):
        total += 40
        roman = roman[4:]
    while roman.startswith('10'):
        total += 10
        roman = roman[2:]
    while roman.startswith('110'):
        total += 9
        roman = roman[3:]
    while roman.startswith('5'):
        total += 5
        roman = roman[1:]
    while roman.startswith('15'):
        total += 4
        roman = roman[2:]
    while roman.startswith('1'):
        total += 1
        roman = roman[1:]

    print(total)


if __name__ == '__main__':
    eval(f'{argv[1]}(*argv[2:])')
