"""
Given String, replace it’s words from lookup dictionary. Read string and dictionary from
keyboard if word is not lookup dictionary print replacement is not possible.
"""
n=int(input("Enter the size of dict: "))
d={}
for i in range(n):
    k=input()
    v=input()
    d[k]=v
print(d)

s=input("Enter the string: ").split()
r=[]
for i in s:
        r.append(d.get(i,i))
res=" ".join(r)
print(str(res))