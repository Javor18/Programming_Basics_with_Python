budget = float(input())
statist = int(input())
price_for_clothes = float(input())

decor_price = budget * 0.10
all_clothing_price = statist * price_for_clothes

if statist > 150 :
   all_clothing_price = all_clothing_price * 0.90

total_price = all_clothing_price + decor_price

diff = abs(total_price - budget)
if total_price > budget:
    print (f"Not enough money!")
    print (f"Wingard needs {diff:.2f} leva more.")
else:
    print (f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
