def readFile(filename):
    """read the comma-separated integer data from the text file
    named filename and return the data in a list"""
    resultForTextFile = [] # list initially empty
    with open(filename, "r") as dataFile:
        for line in dataFile:
            # remove any trailing spaces, comma, and newline
            result += [int(x.strip()) for x in line.rstrip(" ,\n").split(",")]  
    return resultForTextFile

def main():
    list = readFile("Monitor.data")
    print(list)

if __name__ == "__main__":
    main()