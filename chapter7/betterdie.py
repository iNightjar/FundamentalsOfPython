from random import randrange


def random_die(spots):
    """
    Draws a picture of a die with number of spots indicateds.
    spots is the number of spots on the top face.
    """
    print("+---------+")
    if spots == 1:
        print("|         |")
        print("|    *    |")
        print("|         |")

    elif spots == 2:
        print("| *       |")
        print("|         |")
        print("|       * |")

    elif spots == 3:
        print("|        * |")
        print("|     *    |")
        print("| *        |")

    else:
        print(" *** Error: illegal die value *** ")
    print("+---------+")


def roll():
    """returns a pseudorandom number in the range 1 ... 6, inclusive  """

    return randrange(1, 3)


def main():
    """ Simulates the roll  of a die three times"""

    for i in range(1, 4):
        random_die(roll())


main()
