import random

for iterator in range(10):  # loop 10 times
    print("Beginning of loop iteration", iterator)
    try:
        # pick random number between 1 and 4
        randomNumber = random.randint(1, 4)
        if randomNumber == 1:
            print(int('fred'))
        elif randomNumber == 2:
            [][2] = 5
        elif randomNumber == 3:
            print({}[1])
        else:
            print(3/0)

    except ValueError:
        print('cannot convert integer')
    except IndexError:
        print("list index is out of range")
    except ZeroDivisionError:
        print("division by zero not allowed")
    except:
        print("this program has encountered a problem")

    print("End of loop iteration", iterator)
