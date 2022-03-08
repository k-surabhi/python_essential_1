def addition(*args):
    Number_list = []
    for i in inputList:
        z = int(i)
        Number_list.append(z)
    Add = sum(Number_list)
    return Add

def subtraction(*args):
    Number_list = []
    for i in inputList:
        z = int(i)
        Number_list.append(z)
    Subtract = Number_list[0] - sum(Number_list[1:])
    return Subtract

def multiplication(*args):
    return

def division(*args):
    return

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
        select = input("Select(1/2/3/4): ")
        if select in ('1', '2', '3', '4'):
            print("Please enter your values: ")
            user_input = input().split()

        if select == '1':
            Output = addition(user_input)
            print("The sum of your inputs is: ", Output)

        elif select == '2':
            Output = subtraction(user_input)
            print("The difference of you inputs is: ", Output)

        elif select == '3':
            Output = multiplication(user_input)
            print("The product of your inputs is: ", Output)

        elif select == '4':
            Output = division(user_input)
            print("The quotient of your inputs is: ", Output)

        next_calculation = input("Next calculation? (yes/no): ")
        if next_calculation == "no":
            break