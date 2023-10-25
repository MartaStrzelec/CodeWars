#Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.
#As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. 
#For example, the input 'sTreSS' should return 'T'.
#If a string contains all repeating characters, it should return an empty string ("").

def make_dictionary(s):
    dict = {}
    for letter in s:
        if letter.upper() in dict: dict[letter.upper()] += 1
        elif letter.lower() in dict: dict[letter.lower()] += 1 
        else: dict.update({letter : 1})
    return dict

def first_non_repeating_letter(s):
    dict = make_dictionary(s)
    for letter in dict:
        if dict[letter] == 1:
            return letter
    return ''
