import zipfile

zip = zipfile.ZipFile(open('channel.zip','r'))

nothing = 90052
file_name = '%s.txt'
comments = [] #The answer is *in* the zip..

while nothing != 'comments.':
     comments.append(zip.getinfo(file_name % nothing).comment)
     file_content = zip.read(file_name % nothing)
     nothing = file_content.split()[-1]

print "".join(comments)
