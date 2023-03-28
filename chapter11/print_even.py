# generator to print even numbers

def print_even(test_list):
    for iterator in test_list:
        if iterator % 2 == 0:
            yield iterator


test_list = [1, 4, 5, 6, 7]

# printing initial list
print("The original list is : " + str(test_list))

# printing even numbers
print("The even numbers in list are: ", end=' ')
for iterator in print_even(test_list):
    print(iterator, end=' ')
print()