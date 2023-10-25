#Example triangle for n = 5:
# 1                                      
# 2   4   2                              
# 3   6   9   6   3                      
# 4   8   12  16  12  8   4             
# 5   10  15  20  25  20  15  10  5   

#Task: triang_mult(n)  ----> [total_sum, total_even_sum, total_odd_sum]

def count_line(n):
    sum, even_sum, odd_sum = 0, 0, 0
    square = n * n
    a_n = square - n
    k = (a_n - n) / n + 1
    sum = (n + a_n) * k + square
    if n % 2 == 0:
        even_sum = sum
    else:
        odd_sum = a_n * k / 2 + square
        even_sum = sum - odd_sum
    return int(sum), int(even_sum), int(odd_sum)        

def mult_triangle(n):
    total_sum, total_even_sum, total_odd_sum = 0, 0, 0
    for i in range(1,n+1):
        a, b, c = count_line(i) 
        total_sum += a
        total_even_sum += b
        total_odd_sum += c
    return [total_sum, total_even_sum, total_odd_sum]
