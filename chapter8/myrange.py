def myrange(arg1, arg2=None, step=1):
    if arg2 != None:  # Do we have at least two arguments?
        begin = arg1
        end = arg2
    else:  # we must have just one arguement
        begin = 0  # begin value is zero by defautl
        end = arg1
    iterator = begin
    while iterator != end:
        yield iterator
        iterator += step


print('0 to 9: ', end=' ')
for iterator in myrange(10):
    print(iterator, end=' ')
print()


print('1 to 10: ', end=' ')
for iterator in myrange(1, 11):
    print(iterator, end=' ')
print()

print('2 to 18: ', end=' ')
for iterator in myrange(2, 20, 2):
    print(iterator, end=' ')
print()
