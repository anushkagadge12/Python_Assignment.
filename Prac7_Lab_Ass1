def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def mod(a, b):
    if b == 0:
        return "Cannot mod by zero"
    return a % b

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "6":
        break
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    if choice == "1":
        print("Answer is:", addition(a, b))
    elif choice == "2":
        print("Answer is:", subtraction(a, b))
    elif choice == "3":
        print("Answer is:", multiplication(a, b))
    elif choice == "4":
        print("Answer is:", division(a, b))
    elif choice == "5":
        print("Answer is:", mod(a, b))
    else:
        print("Invalid choice")
        