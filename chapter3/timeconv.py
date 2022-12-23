# file timeconv.py
# get the number of seconds

seconds = int(input("Please enter the number of seconds: "))
# First, compute the number of hours in the given number of seconds
# note: integer division with possible truncation
hours = seconds / 3600
seconds = seconds % 3600
minutes = seconds / 60
seconds = seconds % 60

print(hours, minutes, seconds)
