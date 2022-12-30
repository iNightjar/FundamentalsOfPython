# request input from user
num  = int(input('Please enter integer value: '))

if num < 0: 
    num  = 0
if num > 9999:
    num  = 9999

print(end="[")


# extract and print thousnads-place digit
digit = num//1000   # determine the thousands-place digit, floor division
print(digit, end="")
num %= 1000 # discard thousands-place digit


# extract and print hundreds-place 
digit = num//100   
print(digit, end="")  # determine the hundered-place digit, floor division
num %= 100 # discard hundered-place digit


# Extract and print tens-place digit
digit = num//10
 # Determine the tens-place digit
print(digit, end="") # Print the tens-place digit
num %= 10
 # Discard tens-place digit

 # remainder is the one-place digit
print(num, end="")

print("]")