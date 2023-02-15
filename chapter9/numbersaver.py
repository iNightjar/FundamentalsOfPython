"""
uses python's file class to store data to and retrieve data from a text file
"""


def load_data(file):
    """print the elements stored in the text file"""
    # open file to read
    with open(file) as file:
        for line in file:
            print(int(line))


def store_data(file):
    """allows the user to store data to the txt file named file. """
    with open(file, 'w') as file:
        number = 0
        while number != 999:
            number = int(input("Please enter number (999 quits): "))
            if number != 999:
                # convert integer to string to save
                file.write(str(number) + '\n')
            else:
                break


def main():
    """
    Interactive function that allows thee user to create or consume files of numbers. 
    """
    done = False
    while not done:
        cmd = input('S)ave L)oad Q)uit: ')
        if cmd == 'S' or cmd == 's':
            store_data(input("Enter the file name: "))
        elif cmd == 'L' or cmd == 'l':
            load_data(input("Enter filename. "))
        elif cmd == 'Q' or cmd == 'q':
            done = True


if __name__ == '__main__':
    main()
