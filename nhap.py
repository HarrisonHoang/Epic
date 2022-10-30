

choice = input("Enter: ")
while True:
    if choice == 'a' or choice == 'd':
        print("a")
        break
    elif choice != 'a' and choice == 'b':
        print("b")
        break
    elif choice == "c":
        print('c')
        break
    else:
        print("null")
        break