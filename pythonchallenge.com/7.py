import Image

im = Image.open("oxygen.png")

(hsize, vsize) = im.size
print "Image info: %s, %s, %s." % (im.format, vsize, hsize)

message = [0]

for y in range(vsize):
    p = im.getpixel((0,y))
    if p[0] == p[1] == p[2]:
        for x in range(0,hsize,7):
            pixel = im.getpixel((x,y))
            if pixel[0] == pixel[1] == pixel[2]:
                message.append(pixel)
        break

message.remove(0)
collapsed_message =  map(lambda x: x[0], message)
text = ''.join([chr(x) for x in collapsed_message])
print text
for index,char in enumerate(text):
    if char == '[':
        start = index
        break

text2 = text[start+1:-1].split(", ")
print ''.join([chr(int(x)) for x in text2])

"""
Image info: PNG, 95, 629.
smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
integrity
"""
