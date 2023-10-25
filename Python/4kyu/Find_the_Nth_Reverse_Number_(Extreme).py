#Description:
#Reverse Number is a number which is the same when reversed.
#You need to return the nth reverse number. (Assume that reverse numbers start from 0.)
# 1 < n <= 100000000000

import math

def to_palindrome(num, length): #given half of number, returns palindrome with number & reversed number
    if length % 2 == 0:
        return int(str(num) + str(num)[::-1])
    return int(str(num)[:-1] + str(num)[::-1])

def find(length, k, n): #given exact length of palindrome and how many palindromes where find before that length; returns half of nth number
    diff = n-k-1 
    num = pow(10, math.ceil(length / 2) - 1)
    return to_palindrome(num+diff, length)

def count_lvl(number_of_digits): #how many palindromes of given number of digits (length) exsist 
    return 9 * pow(10, math.ceil((number_of_digits - 2) / 2))

def find_reverse_number(n):
    if n < 11:
        return n - 1
    lvl = [1, 10] #[number of digits in palindrome, how many palindromes exsist between length 1 and lvl[0]]
    x = 0
    while n > lvl[1]:
        x = count_lvl(lvl[0] + 1)
        lvl = [lvl[0] + 1, lvl[1] + x]
    return find(lvl[0], lvl[1]-  x, n)
