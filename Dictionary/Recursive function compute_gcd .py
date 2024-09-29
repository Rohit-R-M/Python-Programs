"""
Write recursive function compute_gcd to find the gcd of two numbers.
GCD of 98 and 56 is 14
"""
def compute_gcd(n,m):
    if m==0:
        return n
    else:
        return compute_gcd(m,n%m)
n=int(input("Enter the 1st number: "))
m=int(input("Enter the 2nd number: "))
res=compute_gcd(n,m)
print("GCD: ",res)