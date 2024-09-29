"""
Python – Convert Binary tuple to Integer
Input : test_tup = (1, 1, 0) 
Output : 6 
"""
print("Enter the binary number")
b=input()
print(tuple(b))
l=len(b)
dec=0
for i in b:
    dec+=int(i)*pow(2,l-1)
    l-=1
print(dec)