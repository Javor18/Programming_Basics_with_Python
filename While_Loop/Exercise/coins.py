change = float(input())
coins = change * 100
coins_count = 0

while coins > 0:

    if coins >= 200:
        coins -= 200
        coins_count += 1
    elif coins >= 100:
        coins -= 100
        coins_count += 1
    elif coins >= 50:
        coins -= 50
        coins_count += 1
    elif coins >= 20:
        coins -= 20
        coins_count += 1
    elif coins >= 10:
        coins -= 10
        coins_count += 1
    elif coins >= 5:
        coins -= 5
        coins_count += 1
    elif coins >= 2:
        coins -= 2
        coins_count += 1
    elif coins >= 1:
        coins -= 1
        coins_count += 1
    else:
        break


print(coins_count)
