hours = int(input())
minutes = int(input())

total_minutes = (hours * 60) + minutes + 15

hours = total_minutes // 60
minutes = total_minutes % 60

if hours > 23:
    hours = 0
if minutes > 59:
   minutes = 0

if minutes <= 9:
    print(f'{hours}:0{minutes}')
else :
    print(f'{hours}:{minutes}')