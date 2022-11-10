widght_free_space = int(input())
lenght_free_space = int(input())
height_free_space = int(input())

free_space = widght_free_space * lenght_free_space * height_free_space
total_boxes = 0
total_free_space = 0

command = input()

while command != "Done":

    boxes = int(command)
    total_boxes += boxes


    if free_space < total_boxes:
        break

    command = input()

total_free_space = free_space - total_boxes

if total_boxes <= free_space:
    print(f"{total_free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_free_space)} Cubic meters more.")
