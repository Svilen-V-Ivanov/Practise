def tags(tag):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, *kwargs)
            to_return = f"<{tag}>{result}</{tag}>"

            return to_return

        return wrapper

    return decorator


@tags('h1')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
