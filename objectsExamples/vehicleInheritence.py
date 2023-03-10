from abc import ABCMeta, abstractclassmethod


class Vehicle(object):

    """A vehicle for sale by Jeffco Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheel = 0

    def __inti__(self, wheels, miles, make, model, year, sold_on):
        """return a new car object"""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """returns the price for which we would pay to purchase the vehicle."""
        if self.sold_on is not None:
            return 0.0  # already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """ return the price for which we would pay to purchase the vehicle. """
        if self.sold_on is None:
            return 0.0  # already sold
        return self.base_sale_price - (.10 * self.miles)

    @abstractclassmethod
    def vehicle_type():
        """returns a string representation the type of vehicle this is."""
        pass


class Car(Vehicle):

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """ returns a string representation the type of vehicle this is."""
        return 'car'


class truck(Vehicle):

    base_sale_price = 10000
    wheel = 4

    def vehicle_type(self):
        """return a string representation the type of vehicle this is. """
        return 'truck'


class motorcycle(Vehicle):

    base_sale_price = 4000
    wheel = 2

    def vehicle_type(self):
        """return a string representation the type of vehicle this is. """
        return 'motorcycle'


kai = Car()
print(kai.base_sale_price)
print(kai.vehicle_type())
# print(kai.miles)


print()

cbr = motorcycle()
print(cbr.base_sale_price)
print(cbr.vehicle_type())
# print(kai.miles)
