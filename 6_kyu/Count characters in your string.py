# The main idea is to count all the occurring characters in a string.
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be empty object literal, {}.

def count(s):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic


if __name__ == '__main__':
    print(count('acddatat'))  # -> {'a': 3, 'c': 1, 'd': 2, 't': 2}
