def cache(function):
    numbers = {

    }

    def wrapper(n):
        if n in numbers:
            return numbers[n]
        result = function(n)
        numbers[n] = result

        return result

    wrapper.log = numbers
    return wrapper


@cache
def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


fibonacci(4)
print(fibonacci.log)