def func(a, b, c):
    print('a = ', a, ' b = ', b, ' c = ',  c)


func(1, 2, 3)
dict = {}
dict['b'] = 22
dict['a'] = 11
dict['c'] = 33
func(**dict)  # Pass a dictionary
func(**{'a': 10, 'b': 20, 'c': 30})  # Pass three parameters
