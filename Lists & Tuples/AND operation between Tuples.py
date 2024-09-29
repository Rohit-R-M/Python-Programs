"""
Python – AND operation between Tuples
The original tuple 1 : (10, 4, 5)
The original tuple 2 : (2, 5, 18)
Resultant tuple after AND operation : (2, 4, 0)
"""
a=int(input("Enter the size of tuple 1:"))
b=int(input("Enter the size of tuple 2:"))
t1=[]
for i in range(a):
    x=int(input())
    t1.append(x)
print(tuple(t1))

t2=[]
for i in range(b):
    y=int(input())
    t2.append(y)
print(tuple(t2))

res=[]
for i in range(len(t1)):
    z=t1[i] & t2[i]
    res.append(z)
print("Result= ",tuple(res))