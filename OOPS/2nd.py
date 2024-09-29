"""
2.	Write a python program to simulate bank operations using class concept. 
Consider acc_n,acc_name,balance as attributes and as private. Bank name as class variable
Define below methods
Constructor to create a n bank accounts
Perform following operation based on user choice
Display to display the details of account holder whose acc_n is inputed
Withdraw to perform withdraw operation given the acc_n and amount to be withdraw
Deposit to perform deposit operation given acc_n and amount to be deposited
"""
class Bank:
    def __init__(self,x,y,z):
        self.__acn=x
        self.__aname=y
        self.__bal=z
        Bank.name="SBI"
    def withdraw(self,x,y):
        if self.__acn==x:
            if self.__bal>=y:
                self.__bal-=y
                print("Amount withdrawn")
            else : print("Insufficient balance")
        else : print("Invalid account name")
    
    def deposit(self,x,y):
        if self.__acn==x:
            self.__bal+=y
            print("Amount deposited")
        else : print("Invalid account number")
    def display(self,x):
        if self.__acn==x:
            print("Bank name : ",self.name)
            print("Account holder name : ",self.__aname)
            print("Account number : ",self.__acn)
            print("Balance : ",self.__bal)
n=int(input("Enter number of account holders: "))
li=[]
for i in range(n):
    b1=Bank(i+1,input("Enter your name : "),int(input("Enter your balance : ")))
    print("Your account number :",i+1)
    li.append(b1)
while True:
    print("Enter your choice:")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Display")
    ch=int(input())
    if ch==1:
        n=int(input("Enter your account number : "))
        li[n-1].withdraw(n,int(input("Enter amount to be withdrawn : ")))
    elif ch==2:
        n=int(input("Enter your account number : "))
        li[n-1].deposit(n,int(input("Enter amount to be deposited : ")))
    elif ch==3:
        n=int(input("Enter your account number : "))
        li[n-1].display(n)
    elif ch==4:
        print("Invalid choice")
    else:
        break
