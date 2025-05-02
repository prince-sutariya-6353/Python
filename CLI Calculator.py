# Define a function to add two numbers
def add(x, y):
    return x + y

# Define a function to subtract the second number from the first
def subtract(x, y):
    return x - y

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# Define a function to divide the first number by the second
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"  # Handle division by zero
    return x / y

# Main function to run the calculator
def main():
    print("Simple CLI Calculator")  # CLI = Command Line Interface
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        # Ask the user to choose an operation
        choice = input("Enter choice (1/2/3/4): ").strip()
        # Get the first number from the user
        num1 = float(input("Enter first number: "))
        # Get the second number from the user
        num2 = float(input("Enter second number: "))

        # Perform the operation based on user choice
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid input")  # If user enters anything other than 1-4
    except ValueError:
        # Handle error if user inputs non-numeric values
        print("Invalid number entered.")
    except Exception as e:
        # Handle any unexpected errors
        print("An error occurred:", str(e))

# This ensures the main function runs only when this script is executed directly
if __name__ == "__main__":
    main()
