groups_number = int(input())


musala_count = 0
monblan_count = 0
kili_count = 0
k2_count = 0
everest_count = 0

total_people = 0


for i in range(1, groups_number + 1):
    count_people = int(input())
    total_people += count_people

    if count_people <=5:
        musala_count += count_people
    elif count_people <= 12:
        monblan_count += count_people
    elif count_people <= 25:
        kili_count += count_people
    elif count_people <= 40:
        k2_count += count_people
    else:
        everest_count += count_people

musala_percent = musala_count / total_people * 100
monblan_percent = monblan_count / total_people * 100
kili_percent = kili_count / total_people * 100
k2_percent = k2_count / total_people * 100
everest_percent = everest_count / total_people * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kili_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")