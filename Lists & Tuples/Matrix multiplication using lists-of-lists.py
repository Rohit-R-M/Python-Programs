"""
Read two matrices using list of list and perform multiplication on them
"""
m=int(input("Enter the number of rows: "))
n=int(input("Enter the number of columns: "))
print("Enter the Matrix A")
l1=[]
for i in range(m):
    i1=[]
    for j in range(n):
        x=int(input())
        i1.append(x)
    l1.append(i1)
print(l1)

p=int(input("Enter the number of rows: "))
q=int(input("Enter the number of columns: "))
print("Enter the matrix B")
l2=[]
for i in range(p):
    i2=[]
    for j in range(q):
        y=int(input())
        i2.append(y)
    l2.append(i2)
print(l2)
r=0
l=[]

print("Matrix Multiplication: ")
if(n!=p):
     print("Not")
else:
    result = []
    for i in range(m):
        row = []
        for j in range(q):
            row.append(0)
        result.append(row)

    for i in range(m):
        for j in range(q):
            for k in range(n):
                result[i][j]+=l1[i][k]*l2[k][j]

for i in result:
    print(i)

   