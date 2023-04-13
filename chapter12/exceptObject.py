import random

for iterator in range(10):  # loop 10 times
    print("Beginning of loop iteration", iterator)
    try:
        randomNumber = random.randint(1, 4)
        if randomNumber == 1:
            print(int('fred'))
        elif randomNumber == 2:
            [][2] = 5
        elif randomNumber == 3:
            print({}[1])
        else:
            print(3/0)

    except ValueError as exception:
        print('problem with value  ==> ', type(exception), exception)
    except IndexError as exception:
        print("problem with list ==> ", type(exception), exception)
    except ZeroDivisionError as exception:
        print("problem with division ==> ", type(exception), exception)
    except Exception as exception:
        print("problem with something ==> ", type(exception), exception)

    print("End of loop iteration", iterator)
