"""
Create a dictionary of N students with marks of three subjects as shown below
Student= {2ba17cs011: {‘Math’:50, ‘Phy’:80,’Chem’:65}……………….}
Find the one who scored highest in physics, maths and chemistry subject. Convert dictionary to 
a list of tuple where a each tuple will contain usnnumber, totalmarks and average marks
    [(2ba17cs011,195,65.00)…………………….]
"""

n=int(input("Enter the size of dictionary: "))
m=int(input("Enter the size of inner dict: "))
s={}
for i in range(n):
    pn=input("Enter the USN: ")
    r={}
    for j in range(m):
        q=(input("Enter the Subject Name: "))
        p=int(input("Enter the Marks: "))
        r[q]=p
    s[pn]=r
print(s)

#s= {'2ba17cs000': {'Math':50, 'Phy':80,'Chem':65},'2ba17cs111': {'Math':86, 'Phy':82,'Chem':55}}

hum=""
hmm=0
hup=""
hmp=0
huc=""
hmc=0
for i in s:
    if s[i]['Math']>hmm:
        hmm=s[i]['Math']
        hum=i
    if s[i]['Phy']>hmp:
        hmp=s[i]['Phy']
        hup=i
    if s[i]['Chem']>hmc:
        hmc=s[i]['Chem']
        huc=i
print(hum,"higest in maths",hmm)
print(hup,"higest in physics",hmp)
print(huc,"higest in chem",hmc)

r=[]
for i in s:
    l=[]
    total=s[i]['Math']+s[i]['Phy']+s[i]['Chem']
    avg=total/3
    print(i,"total marks: ",total)
    print(i,"average marks: ",avg)
    l.append(i)
    l.append(total)
    l.append(avg)
    r.append(tuple(l))
print(r)




