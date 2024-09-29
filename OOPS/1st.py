"""
Write a Python program to create a class representing a shopping cart.
Include methods for adding and removing items, and calculating the total price.
"""
class cart:
    def __init__(self):
        self.li=[]
    def add_item(self,x,y,z):
        self.li.append([x,y,z])
        print("Item added to cart")
    def remove_item(self,x):
        for i in self.li:
            if i[0]==x:
                self.li.remove(i)
                print("item removed from cart")
                return
        print("Item does not exists in cart")
    def get_price(self):
        p=0
        for i in self.li:
            p+=i[1]*i[2]
        return p
    def display(self):
        if len(self.li)==0:
            print("Cart is empty")
            return
        print("Item \t Price\tQuantity")
        for i in self.li:
            print(i[0],"\t",i[1],"\t",i[2])
        print("Total \t",self.get_price())
c=cart()
while True:
    print("Enter your choice:")
    print("1. Add")
    print("2. Remove")
    print("3. Price")
    print("4. Clear")
    print("5. Display")
    ch=int(input())
    if ch==1:
        c.add_item(input("Enter item name : "),int(input("Enter its price : ")),int(input("Enter quantity : ")))
    elif ch==2:
        c.remove_item(input("Enter item name : "))
    elif ch==3:
        print("Total price of items in cart : ",c.get_price())
    elif ch==4:
        c.li=[]
        print("Shopping cart cleared")
    elif ch==5:
        c.display()
    elif ch==6:
        print("Invalid choice")
    else:
        break