# def sum(list):
#     """adds up the contents of a list of numeric values.
#     list i sthe list to sum.
#     returns the sum of all elements or zero if the list is empty"""

#     result = 0
#     for item in list:
#         result += item

#     return result


# def make_zero(list):
#     """
#     makes every element in list 1st zero
#     """
#     for iterator in range(len(list)):
#         list[iterator] = 0


# def random_list(list_length):
#     """builds a list of n integers, where each integer
#     is a pseudorandom number in the range 0 .. 99 
#     returns the random list."""
#     import random
#     result = []
#     for iterator in range(list_length):
#         rand = random.randrange(100)
#         result += [rand] 
#     return result

# def main():
#     list = [2,4,6,8]
#     # print the contents of the list
#     print(list)

#     # compute and display sum
#     print(sum(list))

#     # zero out all the elements of list
#     make_zero(list)

#     print(list)

#     print(sum(list))


# main()


list = [1,2,3]
print(list[::-1])
