# use some functions and values from the math modules
from math import sqrt, sin, cos, pi, radians

# get coordinates of the stationary spacecraft, (px, py)
px = float(input("Enter x coordinate of spacecraft: "))
py = float(input("Enter y coordinate of spacecraft: "))

# Get starting coordinates of satellite, (x1, y1)

x = float(input("Enter initial satellite x coordinate: "))
y = float(input("Enter initial satellite y coordinate: "))


# convert 60 degrees to radians to be able to use the trigonometric functions
rads = radians(60)

# precompute the consine and sine of the angle
cos_theta = cos(rads)
sin_theta = sin(rads)

# Make a complete revolution (6*60 = 360 degrees)
for increment in range(0, 7):
    # compute the distance to the satellite
    dist = sqrt((px - x)*(px - x) + (py - x)*(py - y))
    print("Distance to satellite {0:10.2f}  km".format(dist))
    # compute the stellite's new (x,y) location after rotating by 60 degrees
    x, y = x*cos_theta - y*sin_theta, x*cos_theta + y*sin_theta
