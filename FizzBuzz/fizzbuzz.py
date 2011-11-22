
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

def fizzbuzz(x):
    output = ""
    if x % 3 == 0:
        output += "Fizz"
    if x % 5 == 0:
        output += "Buzz"
    return output or x

map(fizzbuzz, range(1,101))


