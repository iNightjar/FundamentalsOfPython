# python program to demonstrate static methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a static method to check if a person is adult or not.
    @staticmethod
    def isAdult(age):
        return age>18
    
    def adult(self, age):
        return age > 18

    


# driver's code
if __name__ == '__main__':
    # res = Person.isAdult(20)
    # print("Is person adult: ", res)

    res = Person('inightjar', 20)
    print(res.isAdult(20))
    # res = Person.isAdult(10)
    # print("Is person adult: ", res)


    res = Person.adult('inightjar', 10)
    
    print(res)