"""
Write a Python program to compute the sum of all the elements of each tuple stored inside a 
list of tuples
Original list of tuples:
[(1, 2), (2, 3), (3, 4)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[3, 5, 7]

"""
m=int(input("Enter the size of the list: "))
p=int(input("Enter the size of tuple: "))
l=[]
for i in range(m):
    l1=[]
    for j in range(p):
        n=(int(input()))
        l1.append(n)
    l.append(tuple(l1))
print(l)
s=[]
for i in range(m):
    sj=sum(l[i])
    s.append(sj)
print(s)
