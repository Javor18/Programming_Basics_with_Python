command = input()
standard_ticket = 0
student_ticket = 0
kid_ticket = 0
total_ticekts = 0
while command != "Finish":
    movie = command
    capacity = int(input())

    count_current_movie_tickets = 0
    command_line = input()

    while command_line != "End":
        type_of_ticket = command_line

        if type_of_ticket == "standard":
            standard_ticket += 1
        elif type_of_ticket == "student":
            student_ticket += 1
        elif type_of_ticket == "kid":
            kid_ticket += 1

        count_current_movie_tickets += 1
        total_ticekts += 1

        if count_current_movie_tickets == capacity:
            break

        command_line = input()

    percent_full = count_current_movie_tickets / capacity * 100
    print(f"{movie} - {percent_full:.2f}% full.")

    command = input()

print(f"Total tickets: {total_ticekts}")

percent_student_ticket = student_ticket / total_ticekts * 100
print(f"{percent_student_ticket:.2f}% student tickets.")

percent_standard_ticket = standard_ticket / total_ticekts * 100
print(f"{percent_standard_ticket:.2f}% standard tickets.")

percent_kid_ticket = kid_ticket / total_ticekts * 100
print(f"{percent_kid_ticket:.2f}% kids tickets.")