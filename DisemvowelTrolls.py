
def disemvowel(string):
    random_string = ''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in string:
        if letter in vowels:
            continue
        random_string += letter
    string = random_string
    return string
