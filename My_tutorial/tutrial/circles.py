from math import pi


def circle_area(rad):
    if rad < 0:
        raise ValueError
    return pi * (rad ** 2)


radii = [2, 0, -3, True]
message = "Area of circles with r = {radius}  is {area}"

for rad in radii:
    A = circle_area(rad)
#    print(message.format(radius=rad, area=A))
