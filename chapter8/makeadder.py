def make_adder():
    loc_val = 2  # local variable definition
    return lambda x: x + loc_val  # returns a function


def main():
    function = make_adder()
    print(function(10))
    print(function(5))

main()
