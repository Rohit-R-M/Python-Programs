l=[]
top = -1
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = int(input("Enter the element to push: "))
        top += 1
        l.append(element)
    elif choice == 2:
        if top == -1:
            print("Stack is empty. Cannot pop.")
        else:
            print("Popped element:", l.pop())
            top -= 1
    elif choice == 3:
        if top == -1:
            print("Stack is empty.")
        else:
            print("Stack elements:")
            for i in range(len(l)-1,-1,-1):
                print(l[i])
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
