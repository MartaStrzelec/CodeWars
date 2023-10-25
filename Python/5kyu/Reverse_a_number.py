#Given a string representing an integer, return a string with every sequence of ascending or descending digits reversed.
#If a digit (or several of the same consecutive digits) is at the junction part of ascending and descending sequence, it should belong to the left part of the junction.
#If the number is a negative number, the symbol '-' does not reverse.
#After reverse, if the digit 0 is in the first place (ignoring the sign), it should be removed:

def remove_zeroes(num): #removes zeroes at the beginning of the str
    i = 0
    while num[i] == '0': i += 1
    return num[i:]

def find_first_difference(num): #decides if sequences are asc/desc
    for i in range(1, len(num)):
        if num[i-1] > num[i]: return False
        if num[i-1] < num[i]: return True
    return True

def find_order(num): #returns [full asc/desc order from the begginning, rest of the sequence]
    if len(num) == 1: return [num, ""]
    ascending = True
    if num[0] > num[1]: ascending = False
    elif num[0] == num[1]: ascending = find_first_difference(num)
    for i in range(1, len(num)):
        if num[i] == num[i-1]: continue
        elif num[i] >= num[i-1] and ascending: continue
        elif num[i] >= num[i-1]: return [num[:i], num[i:]] 
        elif num[i] <= num[i-1] and not ascending: continue
        else: return [num[:i], num[i:]]
    return [num, ""]

def reverse_number(n): 
    negative = False
    if n[0] == "-": #checks if number is negative
        negative = True
        n = n[1:]
    num = ''
    while len(n) > 0:
        x = find_order(n)
        num += (x[0])[::-1]
        n = x[1]
    num = remove_zeroes(num)
    return "-" + num if negative else num
