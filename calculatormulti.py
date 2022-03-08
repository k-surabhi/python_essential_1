def add(n):
    x = 0
    for i in n:
        x = x + int(i)
    return x

def subtract(n):
    x = int(n[0])
    for i in n[1:]:
        x = x - int(i)
    return x

def multiply(n):
    x = int(n[0])
    for i in n[1:]:
        x = x * int(i)
    return x

def division(n):
    x = int(n[0])
    for i in n[1:]:
        x = x / int(i)
    return x

while True:

    print("Select from the following operations :")
    print("1 . Addition")
    print("2 . Subtraction")
    print("3 . Multiply")
    print("4 . Division")

    user_choice = int(input("select 1,2,3,4"))
    a = input("Enter value").split(" ")


    if user_choice == 1:
        print(add(a))

    elif user_choice == 2:

        print(subtract(a))

    elif user_choice == 3:

        print(multiply(a))

    elif user_choice == 4:

        print(division(a))


    next_calculation = input("Next calculation? (yes/no): ")
    if next_calculation == "no":
        break
