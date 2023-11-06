rows, columns = (int(x) for x in input().split(" "))
snake = input()
movement = ''
matrix = []

number = (rows * columns) // len(snake)

for i in range(number + 2):
    movement += snake.strip()

for j in range(rows):
    matrix.append([])

    if (j % 2) == 0:
        for z in range(columns):
            element = movement[0]
            movement = movement[1:]
            matrix[j].append(element)
    else:
        for z in range(columns - 1, -1, -1):
            element = movement[0]
            movement = movement[1:]
            matrix[j].insert(0, element)

for i in range(rows):
    print("".join(str(x) for x in matrix[i]))
