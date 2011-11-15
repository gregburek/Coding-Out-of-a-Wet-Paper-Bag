"""
Write a program that prints the numbers from 1 to 100. But for multiples of
three print “Fizz” instead of the number and for the multiples of five print
“Buzz”. For numbers which are multiples of both three and five print
“FizzBuzz”.
"""

# Loop solution
for x in range(1,101):
    output = ""
    if x % 3 == 0:
        output += "Fizz"
    if x % 5 == 0:
        output += "Buzz"
    if output:
        print output
    else:
        print x

# map solution

def func(x):
    output = ""
    if x % 3 == 0:
        output += "Fizz"
    if x % 5 == 0:
        output += "Buzz"
    return output or x

print map(func(x), range[1,101]


