def nullify(f):
    """ A decorator that guts the functionally of a function"""
    def empty_func(*args, **kwargs):
        """this function deos nothing and returns none"""
        pass
    return empty_func


