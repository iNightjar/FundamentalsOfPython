# # dictionary printing
# dict = {'fred' : 44, 'ella' : 39, 'owen' : 40, 'zoe': 41}
# for iterator in dict.keys():
#     print(iterator, end=' ')

# print()

# dict = {'fred': 44, 'ella': 39, 'owen': 40, 'zoe': 41}
# for iterator in dict:
#     print(iterator, end=' ')
# print()


dict = {'fred': 44, 'ella': 39, 'owen': 40, 'zoe': 41}
for iterator, values in dict.items():
    print(iterator, end=' ')
    print(values, end=' ')
print()


# for iterator, secondIterator in dict.items():
#     print( secondIterator)
# print()

# var = None
# if var:
#     print("hello world!")
