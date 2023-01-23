def tree(height):
    row = 0
    # this stops when row equals the height

    while row < height:
        for count in range(0, height - row):
            print(end=" ")

        for iterator in range(0, (2 * row + 1)):
            print(end="*")

        print()
        row += 1


def main():
    """allows users to draw treess of various heights. """

    height = int(input("Enter height of the tree: "))

    tree(height)


main()
