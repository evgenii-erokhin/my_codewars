# Complete the function that accepts a string parameter, and reverses each word in the string.
# All spaces in the string should be retained.
#
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text: str) -> str:
    """The function that returns an inverted sequence of characters

    :param text: The sequence of characters
    :return: An inverted sequence of characters
    """
    temp_lst = text.split()
    lst = [word[::-1] for word in temp_lst]
    return ' '.join(lst)


if __name__ == '__main__':
    print(reverse_words('This is an example!'))  # -> sihT si na !elpmaxe
