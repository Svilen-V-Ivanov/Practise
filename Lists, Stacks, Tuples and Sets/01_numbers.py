first_set = set(int(x) for x in input().split(" "))
second_set = set(int(x) for x in input().split(" "))
commands = int(input())
commands_dict = {
    "First": first_set,
    "Second": second_set,
}

for i in range(commands):
    command = input().split(" ")
    order = command.pop(0)

    if order == 'Add':
        sequence = command.pop(0)
        for number in command:
            commands_dict[sequence].add(int(number))

    if order == 'Remove':
        sequence = command.pop(0)
        for number in command:
            if int(number) in commands_dict[sequence]:
                commands_dict[sequence].remove(int(number))

    if order == "Check":
        result_one = first_set.issubset(second_set)
        result_two = second_set.issubset(first_set)

        if not result_one and not result_two:
            print("False")
        else:
            print("True")

sorted_first = sorted(first_set)
sorted_second = sorted(second_set)
print(", ".join(str(x) for x in sorted_first))
print(", ".join(str(x) for x in sorted_second))
