def even_odd_filter(**kwargs):
    dictionary_of_numbers = {}
    for key, value in kwargs.items():
        filtered_sequence = []

        if key == 'odd':
            for num in value:
                if int(num) % 2 != 0:
                    filtered_sequence.append(num)
        else:
            for num in value:
                if int(num) % 2 == 0:
                    filtered_sequence.append(num)

        dictionary_of_numbers[key] = filtered_sequence

    filtered_dict = dict(sorted(dictionary_of_numbers.items(), key=lambda x: -len(x[1])))

    return filtered_dict


#Much shorter solution
# def even_odd_filter(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         parity = 0 if key == 'even' else 1
#         filtered = [x for x in value if x % 2 == parity]
#         result[key] = filtered
#
#     return dict(sorted(result.items(), key= lambda x: -len(x[1])))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))