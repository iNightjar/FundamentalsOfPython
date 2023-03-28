def sum(*nums):
    sumOfNumbers = 0
    for num in nums:    # consider each arguement passed to the function
        sumOfNumbers += num
    return sumOfNumbers  # return the sum


print(sum(1,2))
print(sum(1,2,3))
print(sum(1,2,3,4))
print(sum(1,2,3,4,5))