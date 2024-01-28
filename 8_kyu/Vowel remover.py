# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
# Examples
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"
# don't worry about uppercase vowels
# y is not considered a vowel for this kata

def shortcut(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    lst = list(s)
    short = ''
    for letter in lst:
        if letter not in vowels:
            short += letter
    return short

# Другой интересный вариант:
# def shortcut(s):
#     return ''.join(c for c in s if c not in 'aeiou')


if __name__ == '__main__':
    print(shortcut('How are you today?'))  # -> "hw r y tdy?"
