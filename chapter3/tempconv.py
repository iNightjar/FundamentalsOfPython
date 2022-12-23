# #
# File tempconv.py
# #
# Author: Rick Halterman
# #
# Last modified: August 22, 2014
# #
# Converts degrees Fahrenheit to degrees Celsius
# #
# Based on the formula found at
# #
# http: // en.wikipedia.org/wiki/Conversion_of_units_of_temperature
# # Prompt user for temperature to convert and read the supplied value

degreeF = float(input('please enter degree in F: '))

degreeC = (5/9) * (degreeF - 32)

# report the result

print(degreeF, 'degree in Fahrenheit\t', degreeC, 'degree in celsius')
