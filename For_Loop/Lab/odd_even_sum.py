number = int(input())
even_sum = 0
odd_sum = 0
for position in range (1, number + 1):
    current_number = int(input())
    if position % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {odd_sum}')
else:
    diff = abs(odd_sum - even_sum)
    print(f'No')
    print(f'Diff = {diff}')

