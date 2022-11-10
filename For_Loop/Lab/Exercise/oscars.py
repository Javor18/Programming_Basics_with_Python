actor_name = input()
point_from_academy = float(input())
marking_people = int(input())

total_points = point_from_academy


for i in range(1 , marking_people + 1):
    name = input()
    current_points = float(input())

    points = (len(name) * current_points) / 2


    total_points += points
    if total_points >= 1250.5:
        break



if total_points < 1250.5:
        diff = abs(1250.5 - total_points)
        print(f"Sorry, {actor_name} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")

