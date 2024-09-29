"""
Using user defined function check_woodall  find the given number is wired number or not.
formula: w=n*2**(n-1)
"""
def check_woodall(n,x):
    w = (n*(2**n))-1  
    if w == x:
        return 'Yes'
    else:
        return 'No'
x=int(input("Enter the number X: "))
n = int(input("Enter the number n: "))
res = check_woodall(n,x)
print(res)
