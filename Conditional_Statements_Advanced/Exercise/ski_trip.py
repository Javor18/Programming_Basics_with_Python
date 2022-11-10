import math

days = int(input())
room_type = input()
mark = input()
price = 0
total_price = 0
night = days - 1

if room_type == 'room for one person':
    price = 18 * night
elif room_type == 'apartment':
    price = 25 * night
    if days < 10:
        price = price * 0.70
    elif 10 < days < 15:
        price = price * 0.65
    else:
        price = price * 0.50
elif room_type == 'president apartment':
    price = 35 * night
    if days < 10:
        price = price * 0.90
    elif 10 < days < 15:
        price = price * 0.85
    else:
        price = price * 0.80


if mark == 'positive':
    total_price = price*1.25
elif mark == 'negative':
    total_price = price * 0.90

print(f"{total_price:.2f}")