# build a custom list of nonnegative integers specified by the user

def make_list():
    """ builds a list from input provided by the user"""
    result = []
    in_val = 0 # ensure loop is entered at least one
    while in_val >= 0 :
        in_val = int(input("enter integer (-1 quits): "))
        if in_val >= 0:
            result += [in_val]
    return result

print(make_list())