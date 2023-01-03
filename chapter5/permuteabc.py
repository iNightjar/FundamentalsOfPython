# file permuteabc

# the first letter varies from a to c

for first in 'ABC':
    for seconds in 'ABC':
        if seconds != first:
            for third in 'ABC':
                # don't duplicate first or second letter
                if third != first and third != seconds:
                    print(first + seconds + third)
