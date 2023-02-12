"""Returnumbers the nTH fibonacci number"""
def fibonacci(number):
    if number <= 0:
        return  0
    elif number ==1:
        return 1
    else:
        return fibonacci(number-2)+ fibonacci(number-1)

    
print("the fibonacci number is :", fibonacci(3))
