# K -> M
# O -> Q
# E -> G

alphabet = "abcdefghijklmnopqrstuvwxyz"
rot13 = {}
for i, char in enumerate(alphabet):
    rot13[char] = alphabet[i-24]
rot13[' '] = ' '
rot13['.'] = '.'
rot13['('] = '('
rot13[')'] = ')'
rot13["'"] = "'"


def translater(string, rot13):
    convertedString = ''
    for char in string:
        convertedString = convertedString + rot13[char]
    print convertedString

string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

translater(string, rot13)
translater('map.html', rot13)

# output:
# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
# ocr.jvon
