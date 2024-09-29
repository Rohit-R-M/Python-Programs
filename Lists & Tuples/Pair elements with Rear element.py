"""
Pair elements with Rear element in Matrix Row
The original list is : [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
The list after pairing is : [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]
"""
m=int(input("Enter the number of rows: "))
n=int(input("Enter the number of columns: "))
l=[]
for i in range(m):
    l1=[]
    for j in range(n):
        x=int(input())
        l1.append(x)
    l.append(l1)
print(l)
l2=[]
for i in l:
    l3=[]
    for j in range(n-1):
        x=[i[j],i[-1]]
        l3.append(x)
    l2.append(l3)
print(l2)
