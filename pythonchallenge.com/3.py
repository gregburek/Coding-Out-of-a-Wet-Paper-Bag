equality_file = open('equality.html')
#equality_file = ['mkPytpvUSvuPtLFmkeKQIiWNNNaJouCnyPyiaRBSYuvMtBXylHWIKkexawFeNwjIpTJBImSUXiAAAipljptIj']
rare_chars = ''
answer = ''
for line in equality_file:
    for char in line:
        if char.isalpha() == False:
            continue
        if len(rare_chars) < 3 and char.isupper():
            rare_chars = rare_chars + char
        elif len(rare_chars) == 3 and char.islower():
            rare_chars = rare_chars + char
        elif len(rare_chars) > 3 and len(rare_chars) < 7 and char.isupper():
            rare_chars = rare_chars + char
        elif len(rare_chars) == 7 and char.islower():
            answer = answer + rare_chars[3]
            rare_chars = ''
        else:
            rare_chars = ''

print answer

import re
mess = open("re.html").read()
print ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',
     mess))
# output:
#lycdinqffkxedlyaawusnogssotgrw
#linkedlist
