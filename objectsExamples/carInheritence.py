class car(object):
    """A car for sale by Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the car has.
        miles: The integral number of miles driven on the car.
        make: The make of the car as a string.
        model: The model of the car as a string.
        year: The integral year the car was built.
        sold_on: The date the vehicle was sold.
    """

    def __inti__(self, wheels, miles, make, model, year, sold_on):
        """return a new car object"""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """return the sale price for this car as a flaot amount."""
        if self.sold_on is not None:
            return 0.0  # already sold
        return 5000.0 * self.wheels

    def purhace_price(self):
        """return the purchase price for this car as a flaot amount."""
        if self.sold_on is not None:
            return 0.0  # already sold
        return 8000 - (.10 * self.miles)
