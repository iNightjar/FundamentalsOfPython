from random import randint
from functools import partial


# def read_file(filename, arguemnet, value):
#     """
#     Raed arguement form the next file named filename.
#     Returns the number of times value appears in the file.
#     """
#     count, read = 0, 0
#     with open(filename, 'r') as file:
#         for value in file.readlines():
#             read += 1
#             # have we read enough values in yet ?
#             if read > arguemnet:
#                 break
#             # convert text integer into an actual integer
#             if int(value) == value:
#                 count += 1
#     return count


def roll(arguement, value):
    """
    Simulates the roll of a pair of dice n times.
    Returns the number of times a roll resulted in value. 
    """
    count = 0
    for iterator in range(arguement):
        roll = randint(1, 6) + randint(1, 6)
        if roll == value:
            count += 1
    return count


def run_trails(function, times):
    """ Perroms n experiments using function as the source of outcomes.
    counts the number of occurences of each possible outcome.
    """

    for value in range(2, 13):
        print("{:>3}:{:<5}".format(value, function(times, value)))


# compare the actual experiments to the simulation
number_of_trials = 100
print("---- Pseudorandom number rolls ----")
run_trails(roll, number_of_trials)
# print('---- Actual Experimental data ----')
# run_trails(partial(read_file, 'dicedate.data'), number_of_trials)
