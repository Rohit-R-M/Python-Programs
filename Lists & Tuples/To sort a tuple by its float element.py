"""
Write a  Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
"""
n=int(input("Enter the size of list: "))
l=[]
for i in range(n):
    x=input()
    f=input()
    l.append((x,f))
print(l)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i][-1] < l[j][-1]:
            l[i],l[j]=l[j],l[i]
print(l)