def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    return a / b

print("Select from the following operations :")
print("1 . Addition")
print("2 . Subtraction")
print("3 . Multiply")
print("4 . Division")

user_choice = int(input("select 1,2,3,4"))
a = int(input("Enter first number"))
b = int(input("Enter second number"))

if user_choice == 1:
    print(add(a,b))

elif user_choice == 2:

    print(subtract(a,b))

elif user_choice == 3:

    print(multiply(a,b))

elif user_choice == 4:

    print(division(a,b))
