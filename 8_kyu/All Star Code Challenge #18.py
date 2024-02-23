# Create a function that accepts a string and a single character, and returns an integer of the count of occurrences
# the 2nd argument is found in the first one.
#
# If no occurrences can be found, a count of 0 should be returned.
#
# Example^
# str_count("Hello", 'o'); // returns 1
# str_count("Hello", 'l'); // returns 2
# str_count("", 'z'); // returns 0
# Notes
# The first argument can be an empty string
# In languages with no distinct character data type, the second argument will be a string of length 1

def str_count(strng: str, target: str) -> int:
    """Function that accepts a string and a single character.
    And returns an integer of the count of occurrences the 2nd argument is found in the first one.

    :param strng: Sequence of letters
    :param target: Еhe letter to be counted
    :return: The number of occurrences of a character in a string
    """
    count_dict = {}
    if len(strng) > 0:
        for letter in strng:
            if letter not in count_dict:
                count_dict[letter] = 1
            else:
                count_dict[letter] += 1
        return count_dict[target]
    return 0


if __name__ == '__main__':
    print(str_count('', 'l'))