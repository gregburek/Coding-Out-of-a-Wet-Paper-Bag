import requests
import re

number = '12345'
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
count = 0

while True:
    r = requests.get(url % number)
    count += 1
    number = ''.join(re.findall('([1-9])', r.content))
    print "%r: %r" % (count, r.content)
