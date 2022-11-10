members = int(input())

command = input()
all_grades_count = 0
count_grades = 0
while command != "Finish":
    presentation = command
    sum = 0

    for i in range (1 , members + 1):
        current_grade = float(input())
        count_grades += 1
        all_grades_count += current_grade
        sum += current_grade

    avg_grade = sum / members

    print(f"{presentation} - {avg_grade:.2f}.")

    command = input()

total_avg_grades = all_grades_count / count_grades
print(f"Student's final assessment is {total_avg_grades:.2f}.")