#Write a code that receives an array of numbers or strings, goes one by one through it while taking one value out, 
#leaving one value in, taking, leaving, and back again to the beginning until all values are out.

def yes_no(arr):
    output = []
    index = 0
    while len(arr) > 0:
        output.append(arr[index])
        del arr[index]
        if len(arr) != 0:
            index = (index + 1) % len(arr)
    return output
