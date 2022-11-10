import math

movie = input()
movie_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration / 8
relax_time = break_duration / 4

time_for_movie = break_duration - lunch_duration - relax_time

diff = abs(time_for_movie - movie_duration)

if time_for_movie >= movie_duration:
    print (f'You have enough time to watch {movie} and left with {math.ceil(diff)} minutes free time.')
else :
    print (f"You don't have enough time to watch {movie}, you need {math.ceil(diff)} more minutes.")
