needed_money = float(input())
money = float(input())

spend_day = 0
save_day = 0
counter = 0
total_days = 0
total_money = money


while total_money < needed_money:

    if counter == 5:
        break

    action = input()
    amount = float(input())

    if action == "spend":
        spend_day += 1
        counter += 1
        total_money = total_money - amount
        if total_money < 0:
            total_money = 0

    elif action == "save":
        counter = 0
        save_day += 1
        total_money += amount

total_days = save_day + spend_day

if counter == 5:
    print("You can't save the money.")
    print(f"{total_days}")

else:
    print(f"You saved the money for {total_days} days.")


