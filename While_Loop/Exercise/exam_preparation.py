bad_grades = int(input())

bad_tries = 0
sum_bad_grades = 0
last_problem = ""
count_bad_grades = 0
has_failed = False
avg = 0

command = input()

while command != "Enough":


    grade = int(input())

    if grade <= 4:
        bad_tries += 1

    last_problem = command
    count_bad_grades += 1
    sum_bad_grades += grade

    if bad_tries == bad_grades:
        has_failed = True
        break


    command = input()


if has_failed == True:
    print(f"You need a break, {bad_tries} poor grades.")
else:
    avg = sum_bad_grades / count_bad_grades
    print(f"Average score: {avg:.2f}")
    print(f"Number of problems: {count_bad_grades}")
    print(f"Last problem: {last_problem}")

