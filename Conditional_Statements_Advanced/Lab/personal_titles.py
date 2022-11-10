age = float(input())
gender = input()

if gender == 'm':
    if age >= 16:
        print(f'Mr.')
    elif age < 16:
        print(f'Master')
else:
    if age >= 16:
        print(f'Ms.')
    else:
        print(f'Miss')
