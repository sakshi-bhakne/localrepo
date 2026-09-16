#Calcutalor Program:
for i in range(5):
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice (1-4): "))


num1 = int(input("Enter the first number: "));
num2 = int(input("Enter the second number: "));

if choice == "+":
    print("The addition of num1 + num2 = ",num1 + num2)
elif choice == "-":
    print("The substraction of num1 - num2 = ",num1 - num2)
elif choice == "*":
    print("The multiplication of num1 * num2 = ",num1 * num2)
elif choice == "/":
    print("The division of num1 / num2 = ",num1 / num2)

