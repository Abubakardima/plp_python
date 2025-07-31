#basic calculator program
num1 = float(input("Enter your fisrt number: "))
num2 = float(input("Enter your second number: "))
operation = input("Enter operation to perform +,-,*,/: ")

# perform calculaton
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    print("Invalid operations")
print(result)