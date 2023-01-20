def midpoint(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2

    return (x1 + x2) / 2, (y1 + y2) / 2


# get two points from the user
point1 = float(input("Enter first points's x: ")), \
    float(input("Enter first point's y: "))

point2 = float(input("Enter second points's x: ")), \
    float(input("Enter seconds point's y: "))


# compute the midpoint
print(midpoint(point1, point2))
print(type(midpoint(point1, point2)))
