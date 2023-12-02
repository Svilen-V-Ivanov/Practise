from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = f"you called {function.__name__}{args}\n"
        func_value = function(*args, **kwargs)
        return result + f"it returned {func_value}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))