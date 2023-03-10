# display the prime numbers between 2 and 500

# largest potential prime considered

Max = 10 # ,max   >> 10


def main():

    # Each position in the Boolean list indicates
    # if the number of that position is not prime:
    # false means "prime," and true means "composite."
    # Initially all numbers are prime until proven otherwise
    nonprimes = Max * [False]  # Initialize to all False
    print(nonprimes) 
    # First prime number is 2; 0 and 1 are not prime
    nonprimes[0] = nonprimes[1] = True
    # Start at the first prime number, 2.
    for i in range(2, Max + 1):
            # See if i is prime
        if not nonprimes[i]:
            print(i, end=" ")
        # It is prime, so eliminate all of its
        # multiples that cannot be prime
        for j in range(2* i, len(nonprimes) + 1, i):
            print("**** iterator" , i)
            nonprimes[j] = True
    print()  # Move cursor down to next line

main()