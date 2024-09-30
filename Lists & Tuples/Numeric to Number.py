"""
Convert numeric words to numbers
"""
d={'one':1,'two':2,'three':3,'four':4}
n=input("Enter the string: ").split()
for i in n:
    if i in d:
        print(d.get(i),end="")
    else:
        print("not defined")
