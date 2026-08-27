# ==========================
#      PYTHON CALCULATOR
# ==========================

print("=" * 40)
print("      SIMPLE CALCULATOR")
print("=" * 40)

while True:
    print("\nChoose an Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponent (**)")
    print("7. Floor Division (//)")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice == "8":
        print("\nThank you for using the calculator!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("❌ Invalid choice! Please try again.")
        continue

    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == "1":
            result = num1 + num2
            operation = "+"

        elif choice == "2":
            result = num1 - num2
            operation = "-"

        elif choice == "3":
            result = num1 * num2
            operation = "*"

        elif choice == "4":
            if num2 == 0:
                print("❌ Division by zero is not allowed.")
                continue
            result = num1 / num2
            operation = "/"

        elif choice == "5":
            if num2 == 0:
                print("❌ Modulus by zero is not allowed.")
                continue
            result = num1 % num2
            operation = "%"

        elif choice == "6":
            result = num1 ** num2
            operation = "**"

        elif choice == "7":
            if num2 == 0:
                print("❌ Floor division by zero is not allowed.")
                continue
            result = num1 // num2
            operation = "//"

        print("\n----------------------------")
        print(f"Result: {num1} {operation} {num2} = {result}")
        print("----------------------------")

    except ValueError:
        print("❌ Please enter valid numbers.")
