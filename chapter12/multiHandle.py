import random

for iterator in range(10):  # loop 10 times
    print("Beginning of loop iteration", iterator)
    try:
        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            print(int('fred'))
        elif randomNumber == 2:
            [][2] = 5
        else:
            print(3/0)

    except (ValueError, ZeroDivisionError):
        print('problem with integer detected')
    except IndexError:
        print("list index is out of range")
    # except ZeroDivisionError:
    #     print("division by zero not allowed")

    print("End of loop iteration", iterator)
