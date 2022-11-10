count_of_tabs = int(input())
salary = int(input())

copy_salary = salary
for i in range(1 , count_of_tabs + 1):
    web_name = input()

    if web_name == "Facebook":
        copy_salary = copy_salary - 150
    elif web_name == "Instagram":
        copy_salary = copy_salary - 100
    elif web_name == "Reddit":
        copy_salary = copy_salary - 50

if copy_salary <= 0:
    print(f"You have lost your salary.")
else:
    print(copy_salary)

