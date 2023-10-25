#Your task: return the sum of the numbers that occur only once. 

def repeats(arr):
    return sum([num for num in arr if arr.count(num) == 1])
