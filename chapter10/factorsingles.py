number = int(input("Please enter a positive integer: "))
factors = [val for val in range(1, number + 1) if number % val == 0]
print("Factors of ", number, " :: ", factors, '\n')



## factor pairs
factorPairs =  [(val,number//val) for val in range(1, number + 1) if number % val == 0]
print("Factor Pairs of ", number, " :: ", factorPairs, '\n')
