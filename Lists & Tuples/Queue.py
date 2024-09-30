l=[]
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        x=int(input("Enter the element: "))
        l.append(x)
    elif choice==2:
        if l==[]:
            print("under flow")
        else:
            print("removed element: ",l.pop(0))
    elif choice==3:
        if l==[]:
            print("no elements to display")
        else:
            print("queue elements: ",l)
    else:
        break