age = int(input())
price_machine = float(input())
toy_price = int(input())

toy_count = 0
money = 10
sum = 0
brother = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toy_count += 1
    else:
        brother += 1
        sum = sum + money
        money = money + 10

total_toys_price = toy_price * toy_count
saved_money = total_toys_price + sum - brother
diff = abs(saved_money - price_machine)


if saved_money >= price_machine:
    print (f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

