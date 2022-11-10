month = input()
days = int(input())
apartment = 0
studio = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if 7 < days <= 14 :
        studio = studio*0.95
    elif days > 14:
        studio = studio * 0.70
        apartment = apartment * 0.90
elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
    if days > 14:
        studio = studio * 0.80
        apartment = apartment * 0.90
elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    if days > 14:
        apartment = apartment * 0.90

apartment_price = apartment * days
studio_price = studio * days

print (f'Apartment: {apartment_price:.2f} lv.')
print (f'Studio: {studio_price:.2f} lv.')

