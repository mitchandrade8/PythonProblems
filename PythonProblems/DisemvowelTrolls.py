

# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.


# Breakdown: 
    ## Create a fucntion to remove vowels of negative comment

def disemvowel(string):

    ## Create default/blank variable to replace vowels 
    blank_spot = ''

    ## Create an array for Vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    ## Loop through the string given
    for letter in string:
        ## check to see if a letter in the string is a vowel, if so replace with blank and 'continue' looping the rest
        ## of the letters in the string
        if letter in vowels:
            continue
        blank_spot += letter
    string = blank_spot

    ## return the string after replacing vowels with blanks 
    return string

## Personal check to see if this works properly ... will comeback and add tests when i learn how to write units tests in Python.
print(disemvowel("You fucking suck at coding and should quit coding!"))

