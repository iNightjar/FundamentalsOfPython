class car(object):
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    # @classmethod
    def make_car_sound(self, sound):
        return sound

    @classmethod
    def is_motocycle(self):
        return self.wheels == 2


mustang = car('ford', 'mustang')
print(mustang.wheels)
print(car.wheels)
print(mustang.make_car_sound('bobo'))
print(mustang.is_motocycle())
