def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
        select = input("Select(1/2/3/4): ")
        if select in ('1', '2', '3', '4'):
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))

        if select == '1':
            print(number1, "+", number2, "=", add(number1, number2))

        elif select == '2':
            print(number1, "-", number2, "=", subtract(number1, number2))

        elif select == '3':
            print(number1, "*", number2, "=", multiply(number1, number2))

        elif select == '4':
            print(number1, "/", number2, "=", divide(number1, number2))

        next_calculation = input("Next calculation? (yes/no): ")
        if next_calculation == "no":
            break


