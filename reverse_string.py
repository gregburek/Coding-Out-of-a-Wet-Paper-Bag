"""
Write a function to reverse a string
"""

def under_pressure(x):
    # This is terrible
    new_list = list(x)
    rev_list = reversed(new_list)
    return ''.join(rev_list)

def reversed_funv(x):
    length=len(x)
    new_list = []
    for index, obj in enumerate(x):
        x[index] = new_list[length - index]
    return new_list

test_string = 'This is a string'
#print under_pressure(test_string)

print test_string[::-1]
print ''.join([char for char in reversed(test_string)])

def indices(string):
    #broken
    new_list = []
    for index, obj in enumerate(string):
        new_list[len(string)-index-1] = obj
    return ''.join(new_list)

