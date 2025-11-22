num1 = input("enter the first number: ")
num2 = input("enter the second number: ")

operation = input("choose an operation (+, -, *, /): ")

if operation == "*":
    print(float(num1) * float(num2))
elif operation == "-":
    print(float(num1) - float(num2))
elif operation == "+":
    print(float(num1) + float(num2))
elif operation == "/":
    print(float(num1) / float(num2))
else:
    print("you have not choose any operation")