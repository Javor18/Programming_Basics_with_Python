budget = float(input())
video_card_count = int(input())
procesor_count = int(input())
ram_card_count = int(input())

video_card_price = video_card_count * 250

procesor_price = video_card_price * 0.35
procesor_price_per_count = procesor_price * procesor_count

ram_card_price = video_card_price * 0.1
ram_card_price_per_count = ram_card_count * ram_card_price

total_sum = video_card_price + procesor_price_per_count + ram_card_price_per_count

if video_card_count > procesor_count:
    total_sum = total_sum * 0.85

diff = abs(total_sum - budget)
if budget > total_sum:
    print(f'You have {diff:.2f} leva left!')
else:
    diff = abs(total_sum - budget)
    print(f'Not enough money! You need {diff:.2f} leva more!')
