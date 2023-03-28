""" Uses a dictionary to count the number of occurances of each word in a text file."""

# for sys.argv global command line arguements list
import sys


def main():
    """ counts the words in a text file. """
    if len(sys.argv) < 2:  # did the user not supply a file name  ?
        print("Usage: python wordcount <filename>")
        print('     Where <filename> is the name of a text file.')
    else:   # User provided ifle name
        filename = sys.argv[1]
        counters = {}  # Initialize counting dictionary
        with open(filename, 'r')as dataFile:
            content = dataFile.read()
            words = content.split()
            for word in words:
                word = word.upper()
                if word not in counters:
                    counters[word] = 1
                else:
                    counters[word] += 1
            # report the count for each word
            for word, count in counters.items():
                print(word, count)


if __name__ == "__main__":
    main()
