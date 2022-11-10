widght = int(input())
lenght = int(input())

command = input()


total_pieces = widght * lenght
piece_count = 0
piece = 0

while command != "STOP":

    piece = int(command)
    total_pieces = total_pieces - piece

    if total_pieces <= 0:
        break
    command = input()


if total_pieces > 0:
    print(f"{total_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")