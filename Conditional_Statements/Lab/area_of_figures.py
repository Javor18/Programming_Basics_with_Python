type_of_the_figure = input()
from math import pi
result = 0
if type_of_the_figure == "square":
    side = float(input())
    result = side*side
elif type_of_the_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    result = side_a*side_b
elif type_of_the_figure == "circle":
    radius = float(input())
    result = pi * (radius ** 2)
elif type_of_the_figure == "triangle":
    side = float(input())
    high = float(input())
    result = side * high / 2
print(result)