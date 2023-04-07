from random import randint
from functools import partial


def read_file(filename, number, val):
    """
    Reads n integers from the text file named filename,
    Returns the number of times val appears in the file. 
    """
    count, read = 0, 0
    with open(filename, 'r') as file:
        for value in file.readlines():
            read += 1  # have we read enough values in yet?
            if read > number:
                break
            if int(value) == val:  # convert text integers into an actual integers
                count += 1
    return count


def roll(number, val):
    """ 
    Simulates the roll of a pair of dice n times.
    Returns the number of times a roll resulted in val. 
    """
    count = 0
    for iterator in range(number):
        roll = randint(1, 6) + randint(1, 6)
        if roll == val:
            count += 1
    return count


def run_trails(file, number):
    """ 
    Performs n experiments using functions f as the source of
    outcomes. counts the number of occurrances of each possible outocme."""

    for value in range(2, 13):
        print("{:>3}:{:>5}".format(value, file(number, value)))


def main():
    """
    compare the actual experiments to the simulation
    """
    number_of_trials = 100
    print("--- Pseudorandom number rolls ---")
    run_trails(roll, number_of_trials)
    print("--- Actual experimental data ---")
    try:
        run_trails(partial(read_file, 'dicedate.data'), number_of_trials)
    except FileNotFoundError:
        print('Cannot open the file "dicedate.data"')
    except PermissionError:
        print('You do not  have access to the file."dicedate.data"')
    except OSError:
        print('Cannot read the file "dicedate.data"')
    except ValueError:
        print('Data formatting error in "dicedate.data"')


if __name__ == "__main__":
    main()  # Invoke main function
