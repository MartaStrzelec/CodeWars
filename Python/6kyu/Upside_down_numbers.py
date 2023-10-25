# Given a range, return the count of upside down numbers within that range.
#(An upside down number is an integer that appears the same when rotated 180 degrees)

mirror = {
        '9': '6',
        '8': '8',
        '6': '9',
        '1': '1',
        '0': '0'
    }

forbidden_numbers = [2, 3, 4, 5, 7]

def is_upside_down(number):
    number = str(number)
    length = len(number)
    for i in range(int(length / 2) + 1):
        if int(number[i]) in forbidden_numbers: return False
        elif mirror[number[i]] != number[length-i-1]: return False
    return True

def solve(a, b):
    count = 0
    for number in range(a,b):
        if is_upside_down(number):
            count += 1
    return count
