start = int(input())
final = int(input())
magic_number = int(input())
counter = 0
combination_is_found = False

for fist_number in range(start , final + 1):
    for second_number in range (start , final + 1):
        counter += 1
        if fist_number + second_number == magic_number:
            combination_is_found = True
            break
    if combination_is_found == True:
        break

if combination_is_found == True:
    print(f"Combination N:{counter} ({fist_number} + {second_number} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")
