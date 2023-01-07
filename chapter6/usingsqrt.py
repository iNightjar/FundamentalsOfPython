from math import sqrt
x = 16
# pass a literal value and display the result
print(sqrt(16.0))

# pass a variable and display the result
print(sqrt(x))

# pass an expression
print(sqrt(2 * x - 5))

# assign result to variable
y = sqrt(x)
print(y)

# Use result in an expression
y = 2 * sqrt(x + 16) - 4
print(y)

# use the result as argument to a function call
y = sqrt(sqrt(256.0))
print(y)
print(sqrt(int('45')))


__builtins__.print("Hello, Sir")