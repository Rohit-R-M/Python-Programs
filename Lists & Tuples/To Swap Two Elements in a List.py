"""
Python Program to Swap Two Elements in a List
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]
"""
n=int(input("Size of the list: "))
l=[]
print("Enter the number: ")
for i in range(n):
    l.append(int(input()))
print(l)
a=int(input("Enter the postion 1: "))
b=int(input("Enter the position 2: "))
if a<=len(l) and b<=len(l):
    p1=a-1
    p2=b-1
    l[p1],l[p2]=l[p2],l[p1]
print("After swaping: ",l)

