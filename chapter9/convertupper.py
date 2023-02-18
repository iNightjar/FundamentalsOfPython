"""convertupper.py"""


def capitalize(filename):
    """ creates a new file with the prefix 'upper_'
    added to the name of the original file.
    all the alphabetic characters in the new are capitalized.
    this function does no distruc the contents fo the original file."""

    with open(filename, 'r') as infile:
        with open('upper_' + filename, 'w') as outfile:
            for line in infile:
                line = line.strip().upper()
                print(line, file=outfile)


def main():
    capitalize(input("Enter the file name please: "))


if __name__ == '__main__':
    main()