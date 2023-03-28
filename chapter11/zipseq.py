# def gen(number):
#     """generate the first number perfect squares, starting with zero:
#     0,1,4,9,16, ....., (n-1) ^2. """

#     for iterator in range(number):
#         result = iterator ** 2
#         print("** iterator ** 2: ", result)
#         yield result

# for iterator in range(1, 4):
#     print(next(gen(iterator)))
# # for p in zip([10, 20 ,30, 40, 50, 60,], gen(4)):
#     # print(p, end=' ')

# # print()


def fun_generator():
    yield "Hello world!!"
    yield "Geeksforgeeks"


obj = fun_generator()

print(type(obj))

print(next(obj))
print(next(obj))
