def even_odd(*args):
    sequence = []
    list_args = list(args)
    command = list_args.pop(-1)

    if command == 'even':
        for num in list_args:
            if int(num) % 2 == 0:
                sequence.append(num)
    else:
        for num in list_args:
            if int(num) % 2 != 0:
                sequence.append(num)

    return sequence


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
