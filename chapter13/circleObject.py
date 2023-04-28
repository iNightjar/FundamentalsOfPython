class circle:
    """ Respresents a geometric circle object"""
    def __init__(self, center, radius) -> None:
        """ initialize the center's center and radius"""
        # disallow a negative radius
        if radius < 0:
            raise ValueError("Negative Radius.")
        self.center = center
        self._radius = radius

    def get_radius(self):
        """ Return the radius of the circle. """
        return self._radius
    def get_center(self):
        """ Return the coordinatess of the center"""
        return self.center
    
    def get_area(self):
        """ Compute and return the circumference of the circle"""
        from math import pi
        return 2*pi*self._radius
    
    def move(self, pt):
        """ Moves the enter of the circle to point pt"""
        self.center = pt

    def grow(self):
        """ Increases the radius of the circle"""
        self._radius += 1
    
    def shrink(self):
        """ Decreases the radius of the circle;
        does not affect a circle with radius zero"""
        if self._radius > 0:
            self._radius -= 1


# sample = circle((10, 3.4), 5 )
# print(" circle radius is: ", sample.get_radius())