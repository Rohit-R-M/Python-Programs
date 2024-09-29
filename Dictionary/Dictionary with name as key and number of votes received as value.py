# -*- coding: utf-8 -*-
"""
Given an array of names of candidates in an election. A candidate name in the array represents a vote cast to the candidate. 
Convert array of names to a dictionary with name as key and number of votes received as value. Find the name of 
candidates received Max vote. 
"""

n=int(input("Enter the number of voters: "))
l=[]
for i in range(n):
    x=input()
    l.append(x)
print(l)

#l=['ram','ravi','ramesh','ram','raj','ravi','Ramesh','raj','ramesh','ram']
ele_data={}
for i in l:
    if i in ele_data:
        ele_data[i]+=1
    else:
        ele_data[i]=1
print(ele_data)

m_v=max(ele_data,key=ele_data.get)
print(m_v)