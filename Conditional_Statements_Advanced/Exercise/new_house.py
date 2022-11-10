flowers_type = input()
flowers_count = int(input())
budget = int(input())
price = 0

rose_price = 5
dalia_price = 3.80
tulip_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

if flowers_type == 'Roses':
    price = flowers_count*rose_price
    if flowers_count > 80:
        price = price * 0.9

elif flowers_type == 'Dahlias':
    price = flowers_count * dalia_price
    if flowers_count > 90:
        price = price * 0.85
elif flowers_type == 'Tulips':
    price = flowers_count * tulip_price
    if flowers_count > 80:
        price = price * 0.85
elif flowers_type == 'Narcissus':
    price = flowers_count * narcissus_price
    if flowers_count < 120:
        price = price * 1.15
elif flowers_type == 'Gladiolus':
    price = flowers_count * gladiolus_price
    if flowers_count < 80:
        price = price * 1.20

diff = abs(price - budget)

if price <= budget:
    print (f'Hey, you have a great garden with {flowers_count} {flowers_type} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')