# Simple menu program (menu.py): use a while loop that shows a menu (1. Add, 2. Subtract, 3. Exit), asks for a choice, and keeps running until the user chooses Exit.
while True:
    print("Menu:")
    print("1.Add")
    print("2.Substract")
    print("3.Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print(f"The difference of {num1} and {num2} is {result}")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")