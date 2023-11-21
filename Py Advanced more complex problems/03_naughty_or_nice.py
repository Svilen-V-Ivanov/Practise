def naughty_or_nice_list(names_list, *args, **kwargs):
    nice_kids = []
    naughty_kids = []

    def find_child(value_to_identify, list, type):
        count = 0
        kid = None
        if type == 'number':
            value_to_identify = int(value_to_identify)
        elif type == 'name':
            value_to_identify = str(value_to_identify)

        for item in list:
            if value_to_identify in item:
                kid = item
                count += 1

        if count == 1:
            list.remove(kid)
        else:
            kid = None

        return kid

    for combination in args:
        position, status = combination.split("-")
        child = find_child(position, names_list, 'number')

        if not child:
            continue

        if status == 'Nice':
            nice_kids.append(child)
        elif status == 'Naughty':
            naughty_kids.append(child)

    for key, value in kwargs.items():
        child = find_child(key, names_list, 'name')

        if not child:
            continue

        if value == 'Nice':
            nice_kids.append(child)
        elif value == 'Naughty':
            naughty_kids.append(child)

    string = ''

    if nice_kids:
        all_names = []
        string += 'Nice: '
        for child in nice_kids:
            all_names.append(child[1])

        string += ', '.join(str(x) for x in all_names) + '\n'

    if naughty_kids:
        all_names = []
        string += 'Naughty: '
        for child in naughty_kids:
            all_names.append(child[1])

        string += ', '.join(str(x) for x in all_names) + '\n'

    if names_list:
        all_names = []
        string += 'Not found: '
        for child in names_list:
            all_names.append(child[1])

        string += ', '.join(str(x) for x in all_names)

    return string


# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))

# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))