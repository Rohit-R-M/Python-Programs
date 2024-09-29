"""
9. Python : Extract elements with Frequency greater than K
nput : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
Output : [4, 3] 
Explanation : Both elements occur 4 times. 
Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2 
Output : [4, 3, 6] 
Explanation : Occur 4, 3, and 3 times respectively.
"""
k=int(input("Enter the frequency: "))
n=int(input("Enter the size of list: "))
l=[]
for i in range(n):
    l.append(int(input()))
print(l)
t=[]
for j in range(n):
    c=l.count(l[j])
    if c>=k and l[j] not in t:
        t.append(l[j])
print(t)
