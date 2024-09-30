"""
Read a list of tuples and get a list, sorted in increasing order by the last element in each tuple from
           a given list of non-empty tuples.
           Sample List: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
           Expected Result: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""
m=int(input("Enter the size of list:"))
n=int(input("Enter the size of tuples: "))
l=[]
for i in range(m):
    l1=[]
    for j in range(n):
        x=int(input())
        l1.append(x)
    l.append(tuple(l1))
print(l)

for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j][-1]>l[j+1][-1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)