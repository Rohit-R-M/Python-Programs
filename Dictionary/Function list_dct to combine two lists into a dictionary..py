# -*- coding: utf-8 -*-
"""
Write a function list_dct to combine two lists into a dictionary.
The elements of the first one serve as keys and the elements of the second one serve as values
"""
def list_dict(l1,l2,n):
    d={}
    for i in range(n):
        d[l1[i]]=l2[i]
    print(d)
    
n=int(input("Enter the size of list1 that is equal to list2: "))
print("Enter the key number in integer: ")
l1=[]
for i in range(n):
    a=int(input())
    l1.append(a)
print(l1)
print("Enter the value: ")
l2=[]
for i in range(n):
    b=input()
    l2.append(b)
print(l2)
list_dict(l1,l2,n)