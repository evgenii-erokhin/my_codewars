# Write a function to convert a name into initials.
# This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

def abbrev_name(name: str) -> str:
    name_ls = name.split()
    first_name = name_ls[0][0]
    last_name = name_ls[1][0]
    abbrev = first_name + '.' + last_name
    return abbrev.upper()

# альтернативный  лучший вариант
# def abbrevName(name):
#     return '.'.join(w[0] for w in name.split()).upper()


if __name__ == '__main__':
    print(abbrev_name('sam harris'))
