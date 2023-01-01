# some userful conversion factors
seconds_per_minute = 60
seconds_per_hour = 60 * seconds_per_minute  # 3600

# get user input in seconds
seconds = int(input("Please enter the number of seconds: "))

# First, compute the number of hours in the given number of seconds
hours = seconds // seconds_per_hour  # flour the output result to number of hours

# compute the remaining seconds after the hours are accounted for
seconds = seconds % seconds_per_hour

# calculate the minutes
# flour the output result to number of minutes
minutes = seconds // seconds_per_minute

# compute the remaining seconds after the minutes are accounted for
seconds = seconds % seconds_per_minute

print(hours, end='')
# Decide between singular and plural form of hours
if hours == 1:
    print(" hour ", end='')
else:
    print(" hours ", end='')


print(minutes, end='')
# Decide between singular and plural form of minutes
if minutes == 1:
    print(" minute ", end='')
else:
    print(" minutes ", end='')


print(seconds, end='')
# Decide between singular and plural form of seconds
if seconds == 1:
    print(" second")
else:
    print(" seconds")
