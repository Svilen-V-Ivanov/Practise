def grocery_store(**kwargs):
    groceries = {}

    for key, value in kwargs.items():
        if key in groceries.keys():
            groceries[key] += int(value)
        else:
            groceries[key] = int(value)

    groceries = dict(sorted(groceries.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

    result = '\n'.join(f"{key}: {value}" for key, value in groceries.items())

    return result

#The Very shortened version of that solution is:
# def grocery_store(**kwargs):
#     sorted_groceries = [f"{key}: {value}" for key, value in \
#                         sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))]
#     return '\n'.join(sorted_groceries)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
