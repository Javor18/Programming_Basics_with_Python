budget = float(input())
season= input()

destination = ""
expenses= 0
place = ""

if budget <=100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        expenses = budget * 0.3
    elif season == "winter":
        place = "Hotel"
        expenses = budget * 0.7
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place ="Camp"
        expenses = budget * 0.4
    elif season == "winter":
        place = "Hotel"
        expenses = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    expenses = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{place} - {expenses:.2f}')



