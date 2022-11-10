start_number = int(input())
bonus = 0

if start_number <= 100:
    bonus = 5
elif start_number <= 1000:
    bonus = start_number * 0.20
else :
    bonus = start_number * 0.10

if start_number % 2 == 0:
    bonus = bonus + 1
elif start_number % 10 == 5:
    bonus = bonus + 2

print (bonus)
print (start_number + bonus)