def fill_the_box(height, length, width, *args):
    volume = int(height) * int(length) * int(width)
    count = 0

    for cube in args:
        if cube == 'Finish':
            break
        count += int(cube)

    if count > volume:
        return f"No more free space! You have {count - volume} more cubes."
    else:
        return f"There is free space in the box. You could put {volume - count} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
