import math
import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def logarithm(x):
    if x <= 0:
        raise ValueError("Cannot calculate logarithm of non-positive number")
    return math.log10(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("Cannot calculate natural logarithm of non-positive number")
    return math.log(x)

def display_menu():
    print("\nScientific Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Logarithm (log10)")
    print("11. Natural Logarithm (ln)")
    print("12. Constants (π, e)")
    print("13. Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-13): ")
            
            if choice == '13':
                print("Thank you for using the calculator!")
                sys.exit()
                
            elif choice == '12':
                print(f"π (pi) = {math.pi}")
                print(f"e = {math.e}")
                continue
                
            elif choice in ['1', '2', '3', '4', '5']:
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                
                if choice == '1':
                    print(f"Result: {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {divide(num1, num2)}")
                elif choice == '5':
                    print(f"Result: {power(num1, num2)}")
                    
            elif choice in ['6', '7', '8', '9', '10', '11']:
                num = get_number("Enter number: ")
                
                if choice == '6':
                    print(f"Result: {square_root(num)}")
                elif choice == '7':
                    print(f"Result: {sine(num)}")
                elif choice == '8':
                    print(f"Result: {cosine(num)}")
                elif choice == '9':
                    print(f"Result: {tangent(num)}")
                elif choice == '10':
                    print(f"Result: {logarithm(num)}")
                elif choice == '11':
                    print(f"Result: {natural_log(num)}")
            
            else:
                print("Invalid choice. Please select a number between 1 and 13.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main() 