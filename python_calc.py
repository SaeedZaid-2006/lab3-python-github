
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "cannot divide by zero"
    return a / b

def check_even_odd(n):
    if n != int(n):
        return "decimal number, so it is not even or odd"
    if int(n) % 2 == 0:
        return "Even"
    else:
        return "Odd"
def percentage(a, b):
    if b == 0:
        return "Error: cannot calculate percentage of zero"
    return (a / b) * 100

def get_numbers():
    while True:
        try:
            x = float(input("Enter first number:"))
            y = float(input("Enter second number:"))
            return x, y
        except ValueError:
            print("Invalid input, please enter numbers only.")

def show_menu():
    print("\nCalculator Menu:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

def main():
    print("Welcome to the Improved Python Calculator!")
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice, try again.")
            continue

        num1, num2 = get_numbers()

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        elif choice == "5":
            print(num1, "is", check_even_odd(num1))
            print(num2, "is", check_even_odd(num2))
        elif choice == "6":
            result = percentage(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(num1, "is", result, "% of", num2)

main()