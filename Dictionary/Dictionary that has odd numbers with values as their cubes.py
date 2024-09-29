"""
Prepare a dictionary that has odd numbers from 1 to 30 as keys with values as their cubes
"""
n=int(input("Enter the number: "))
d={}
for i in range(1,n+1):
    if(i%2!=0):
        s=i**3
        d[i]=s
print(d)