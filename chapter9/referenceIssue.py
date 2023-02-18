class baseObject:
    initialized = False

    def __init__(self) -> None:
        baseObject._initialize()
    
    @classmethod
    def _initialize(cls):
        print("cls.initialized = " + str(cls.initialized))
        if not cls.initialized:
            cls.x = 1
            cls.initialized = True

class objectOne(baseObject):
    @classmethod
    def double_x(cls):
        baseObject.x = baseObject.x * 2
        print(cls.x)


class objecttwo(baseObject):
    @classmethod
    def triple_x(cls):
        baseObject.x = baseObject.x * 3
        print(cls.x)

if __name__ == '__main__':
    # print(baseObject.x)
    obj1 = objectOne()
    obj1.double_x()
    obj2 = objecttwo()
    obj2.triple_x()

