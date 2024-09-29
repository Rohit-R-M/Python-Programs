"""
Python Extract Symmetric Tuples
Input : test_list = [(6, 7), (2, 3), (7, 6)] 
Output : {(6, 7)} 
"""
l=[]
for i in range(3):
    l1=[]
    for j in range(2):
        n=(int(input()))
        l1.append(n)
    l.append(tuple(l1))
print(l)
for i in range(3):
    for j in range(i+1,3):
        if sum(l[i])==sum(l[j]):
            print(tuple(l[i]))