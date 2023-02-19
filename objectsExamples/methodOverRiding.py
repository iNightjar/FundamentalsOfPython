class firstClass:
    def explore(self):
        print("explore() method from class 'firstClass'")


class secondClass(firstClass):
    def explore(self):
        super().explore()  # calling th first class method first
        print("explore() method from class 'secondClass'")


objectB = secondClass()
objectB.explore()
