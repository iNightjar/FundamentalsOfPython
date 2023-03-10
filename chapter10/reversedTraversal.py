nums = [2, 4, 6, 8]
# Print last element to first (zero index) element
# for iteration in reversed(range()):
# print(nums[iteration])


def my_reversed(list):
    """generate the elements of list from back to front.
    works like the built-in reversed generator function"""
    for iteration in range(len(list)-1, -1, -1):
        print(list[iteration])
        yield (list[iteration])


print(my_reversed(nums))
