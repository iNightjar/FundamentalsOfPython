# Print primes till max_value

maxValue = int(input("Enter max vlaue to calculate Primes. "))

# simplest using for loop and if/else
for value in range(2, maxValue + 1):
    for iterator in range(2, value):
        if value % iterator == 0:
            break
    else:
        print(value, end=" ")
print()
