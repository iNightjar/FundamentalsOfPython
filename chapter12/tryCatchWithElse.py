def func1():
    try:
        print('try code')
    except:
        print(('no exception raised code '))
    else:
        print('no exception handling code ')
        x = int('a') # Raise an exception


def func2():
    try:
        print("try code")
        print("no exception raised code")
        x = int('a')  # raises an exception
    except:
        print("exception handling code")


print("Calling func2")
func2()
print('--------------------')
print("Calling func1")
func1()
