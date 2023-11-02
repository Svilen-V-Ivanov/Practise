number = int(input())
longest_intersection = []
intersection = 0

for i in range(number):
    base_intersection = []
    range_dict = {}
    sequence = input()
    first, second = sequence.split('-')
    first_start, first_end = (int(x) for x in first.split(','))
    second_start, second_end = (int(x) for x in second.split(','))

    for j in range(first_start, first_end + 1):
        range_dict[j] = 1

    for z in range(second_start, second_end + 1):
        if z in range_dict.keys():
            range_dict[z] += 1
        else:
            range_dict[z] = 1

    for key, value in range_dict.items():
        if value == 2:
            base_intersection.append(key)

    if len(base_intersection) > intersection:
        intersection = len(base_intersection)
        longest_intersection = base_intersection

#A shorter solution is to make them in sets and do intersection, not with dicts, as follows:
# first_set = set(range(one, two + 1))
#     second_set = set(range(three, four + 1))
#
#     intersected_set = first_set.intersection(second_set)
#     if len(intersected_set) > len(longest_set):
#         longest_set = intersected_set

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")

