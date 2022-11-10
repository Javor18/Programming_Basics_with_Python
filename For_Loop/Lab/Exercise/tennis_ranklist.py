import math

games = int(input())
starting_points = int(input())

points = 0
win_count = 0

for i in range(1 , games + 1):
    level = input()

    if level == 'W':
        win_count += 1
        points = points + 2000
    elif level == 'F':
        points = points + 1200
    elif level == 'SF':
        points = points + 720

total_points = points + starting_points

print(f"Final points: {total_points}")

avg_points = math.floor(points / games)

print(f"Average points: {avg_points}")

win_percent = win_count / games * 100

print(f"{win_percent:.2f}%")