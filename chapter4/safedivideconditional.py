# Get the dividend and divisor from the user
divident = int(input("Enter Divident: "))
divisor = int(input("Enter divisor: "))

# We want to divide only if divisor is not zero, otherwise
# We will print an error message

msg = divident/divisor is divisor if divisor != 0 else 'Error, cannot divide by zero. '
print(msg, divident/divisor)
