# find rare characters in the mess below:

ocr_file = open('ocr.html')
charFreq = {}
rare_chars = ''
for line in ocr_file:
    for char in line:
        if char.isalpha():
            rare_chars = rare_chars + char
        try:
            charFreq[char] += 1
        except KeyError:
            charFreq[char] = 1

for char in charFreq:
    print char, charFreq[char]

print rare_chars

# Output 
#
# 1220
# ! 6079
# # 6115
# % 6104
# $ 6046
# & 6043
# ) 6186
# ( 6154
# + 6066
# * 6034
# @ 6157
# [ 6108
# ] 6152
# _ 6112
# ^ 6030
# a 1
# e 1
# i 1
# l 1
# q 1
# u 1
# t 1
# y 1
# { 6046
# } 6105
# equality
