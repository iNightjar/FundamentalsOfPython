# get two integers form the user

dividend = int(input('please enter the number to divide: '))
divisor = int(input('please enter dividend: '))
# if possible, divide them and report the result

if divisor != 0: 
    result = dividend / divisor # organizing the code
    print( dividend, '/', divisor, '=', result)

else:
    print("zero is not allowed as divisor. ")

print('Program Finished')
