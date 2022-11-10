trip_price = float(input())
puzle = int(input())
talking_toy = int(input())
bear = int(input())
minion = int(input())
truck = int(input())


puzle_price = puzle * 2.60
talking_toy_price = talking_toy * 3
bear_price = bear * 4.10
minion_price = minion * 8.20
truck_price = truck * 2

total_price = puzle_price + talking_toy_price + bear_price + minion_price + truck_price
total_count = puzle + talking_toy + bear + minion + truck

if total_count >= 50:
    total_price = total_price * 0.75

total_price = total_price * 0.90

diff = abs(trip_price - total_price)
if trip_price <= total_price:
    print (f'Yes! {diff:.2f} lv left.')
else :
    print (f'Not enough money! {diff:.2f} lv needed.')