from functools import wraps


def make_bold(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        output = f"<b>{result}</b>"

        return output

    return wrapper


def make_italic(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        output = f"<i>{result}</i>"

        return output

    return wrapper


def make_underline(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        output = f"<u>{result}</u>"

        return output

    return wrapper



@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))