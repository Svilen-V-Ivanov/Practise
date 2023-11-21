# FIXED CODE AND GREATLY REDUCED LENGTH

def is_inside(position, row, col):
    p_row, p_col = position

    return 0 <= p_row < row and 0 <= p_col < col


def next_position(direction, steps, position):
    player_row, player_col = position

    if direction == 'up':
        player_row -= steps
    if direction == 'down':
        player_row += steps
    if direction == 'left':
        player_col -= steps
    if direction == 'right':
        player_col += steps

    return [player_row, player_col]


def valid_movement(direction, steps, player_position):
    one, two, three = 0, 0, 0
    way = ''
    if direction == 'up':
        one, two, three = player_position[0], player_position[0] - steps, player_position[1]
        way = 'vertical'
    if direction == 'down':
        one, two, three = player_position[0], player_position[0] + steps, player_position[1]
        way = 'vertical'
    if direction == 'left':
        one, two, three = player_position[1], player_position[1] - steps, player_position[0]
        way = 'horizontal'
    if direction == 'right':
        one, two, three = player_position[1], player_position[1] + steps, player_position[0]
        way = 'horizontal'

    return one, two, three, way


rows, cols = [int(x) for x in input().split(", ")]
field = []

player_position = [0, 0]
total_items = {
    'D': 0,
    'G': 0,
    'C': 0
}
for i in range(rows):
    field.append(input().split(" "))
    for j in range(cols):
        if field[i][j] == 'Y':
            player_position = [i, j]

        if field[i][j] in 'DGC':
            total_items[field[i][j]] += 1


collected_items = {
    'D': 0,
    'G': 0,
    'C': 0
}
items = {
    'D': 'Christmas decorations',
    'G': 'Gifts',
    'C': 'Cookies'
}

is_completed = False
while True:
    order = input()

    if order == 'End':
        break
    else:
        direction, steps = order.split('-')
        steps = int(steps)

    field[player_position[0]][player_position[1]] = 'x'
    future_position = next_position(direction, steps, player_position)

    if is_inside(future_position, rows, cols):
        player_row, player_col = player_position

        if direction == 'up':
            for i in range(player_row, player_row - steps - 1, -1):
                if field[i][player_col] in 'DGC':
                    collected_items[field[i][player_col]] += 1
                field[i][player_col] = 'x'

                if collected_items == total_items:
                    player_position = [i, player_col]
                    is_completed = True
                    break

            if is_completed:
                break
            player_position = future_position

        elif direction == 'down':
            for i in range(player_row, player_row + steps + 1):
                if field[i][player_col] in 'DGC':
                    collected_items[field[i][player_col]] += 1
                field[i][player_col] = 'x'

                if collected_items == total_items:
                    player_position = [i, player_col]
                    is_completed = True
                    break

            if is_completed:
                break
            player_position = future_position

        elif direction == 'left':
            for i in range(player_col, player_col - steps - 1, -1):
                if field[player_row][i] in 'DGC':
                    collected_items[field[player_row][i]] += 1
                field[player_row][i] = 'x'

                if collected_items == total_items:
                    player_position = [player_row, i]
                    is_completed = True
                    break

            if is_completed:
                break
            player_position = future_position

        elif direction == 'right':
            for i in range(player_col, player_col + steps + 1):
                if field[player_row][i] in 'DGC':
                    collected_items[field[player_row][i]] += 1
                field[player_row][i] = 'x'

                if collected_items == total_items:
                    player_position = [player_row, i]
                    is_completed = True
                    break

            if is_completed:
                break
            player_position = future_position
    else:
        player_row, player_col = player_position
        if direction == 'up':
            start = player_row
            for i in range(steps):
                start -= 1
                if start < 0:
                    start = rows - 1
                if field[start][player_col] in 'DGC':
                    collected_items[field[start][player_col]] += 1
                field[start][player_col] = 'x'
                if collected_items == total_items:
                    player_position = [start, player_col]
                    is_completed = True
                    break

            if is_completed:
                break
            player_position = [start, player_col]

        if direction == 'down':
            start = player_row
            for i in range(steps):
                start += 1
                if start > (rows - 1):
                    start = 0
                if field[start][player_col] in 'DGC':
                    collected_items[field[start][player_col]] += 1
                field[start][player_col] = 'x'
                if collected_items == total_items:
                    player_position = [start, player_col]
                    is_completed = True
                    break

            if is_completed:
                break
            player_position = [start, player_col]

        if direction == 'left':
            start = player_col
            for i in range(steps):
                start -= 1
                if start < 0:
                    start = cols - 1
                if field[player_row][start] in 'DGC':
                    collected_items[field[player_row][start]] += 1
                field[player_row][start] = 'x'
                if collected_items == total_items:
                    player_position = [player_row, start]
                    is_completed = True
                    break

            if is_completed:
                break
            player_position = [player_row, start]

        if direction == 'right':
            start = player_col
            for i in range(steps):
                start += 1
                if start > cols - 1:
                    start = 0
                if field[player_row][start] in 'DGC':
                    collected_items[field[player_row][start]] += 1
                field[player_row][start] = 'x'
                if collected_items == total_items:
                    player_position = [player_row, start]
                    is_completed = True
                    break

            if is_completed:
                break
            player_position = [player_row, start]

field[player_position[0]][player_position[1]] = 'Y'

if is_completed:
    print("Merry Christmas!")

print("You've collected:")

for key, value in collected_items.items():
    print(f"- {value} {items[key]}")

for i in range(rows):
    print(" ".join(str(x) for x in field[i]))
