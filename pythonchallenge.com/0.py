# 2^38

x = 2
for i in range(1,38):
    x = x*2
print "2^%r = %r" % (i+1, x)

def exp(base, exponent):
    if exponent == 0:
        return 1
    return base * exp(base, exponent-1)

print exp(2, 38)

# Output:
# 2^38 = 274877906944
# 274877906944
