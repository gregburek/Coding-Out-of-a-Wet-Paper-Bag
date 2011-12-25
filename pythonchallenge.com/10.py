a=['1']
for i in range(30):
    elem=a[-1]+'?'
    next=[]
    start=0
    for end in range(len(elem)):
        if elem[end]!=elem[start]:
            next.append(str(end-start)+elem[start])
            start=end
        a.append(''.join(next))
print len(a[-1])

"""
5808
"""
