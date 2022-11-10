import math

record_in_seconds = float(input())
distance_in_metres = float (input())
time_for_meter = float(input())

swimming_time = distance_in_metres * time_for_meter

water_resistance = math.floor (distance_in_metres / 15) * 12.5
total_time = swimming_time + water_resistance

if total_time < record_in_seconds :
    print (f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else :
    diff = abs(total_time - record_in_seconds)
    print (f'No, he failed! He was {diff:.2f} seconds slower.')
