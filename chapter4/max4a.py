# Get input values from user
print("Please enter four enterger values")
num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))
num3 = int(input("enter number3: "))
num4 = int(input("enter number4: "))


# compute the maximum value
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    max = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    max = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    max = num3
else:  # the maximum must be num4 at this point
    max = num4

# report the result
print("The maximum number entered was: ", max)
