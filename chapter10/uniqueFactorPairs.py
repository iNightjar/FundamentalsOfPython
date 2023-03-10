import math

number = int(input("Please enter a positive integer: "))
factors = [(val, number//val)
           for val in range(1, round(math.sqrt(number)) + 1) if number % val == 0]
print("Factor pairs of ", number, " :: ", factors)
