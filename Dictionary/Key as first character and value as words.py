"""
Read a line of text and create a dictionary with key as first character and value as words starting
                with that character S={‘s’:  [‘sorry’,’string’]…..}

"""
s=input("Enter the string: ").split()
print(s)
d={}
for i in s:
    if i[0] not in d.keys():
        d[i[0]]=[]
        d[i[0]].append(i)
    else:
        if i[0] not in d[i[0]]:
            d[i[0]].append(i)
print(d)