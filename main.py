fname_arr = []
lname_arr = []
Age_arr = []

number_of_employees_str = input("Enter number of employees:")
number_of_employee = int(number_of_employees_str)

for index in range(number_of_employee):
    fname = input("Enter first name:")
    fname_arr.append(fname)
    lname = input("Enter last name:")
    lname_arr.append(lname)
    Age_str = input("Enter age of employee:")
    Age = int(Age_str)
    Age_arr.append(Age)

print("First name\t Last Name\t Age")

for index in range(number_of_employee):
    print(f"{fname_arr.pop(index).capitalize()}  \t"+ f" {lname_arr.pop(index).capitalize()}  \t"+ f" {Age_arr.pop(index)}  \t")





