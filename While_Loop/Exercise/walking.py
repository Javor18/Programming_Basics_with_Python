command = input()
total_steps = 0

while command != "Going home":


    steps = int(command)
    total_steps += steps

    if total_steps >= 10000:
       break

    command = input()


if command == "Going home":
    home_steps = int(input())
    total_steps += home_steps

diff = abs(total_steps - 10000)


if total_steps >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")




