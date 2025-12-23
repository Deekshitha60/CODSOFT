# Simple Calculator - Task 2 (CodSoft Internship)

print("===== SIMPLE CALCULATOR =====")

while True:
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Exiting Calculator. Thank you!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Please select from 1-5.")
        continue

    # Take two numbers from user
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print("Result:", result)