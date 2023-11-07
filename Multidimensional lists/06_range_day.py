def is_inside(next_row, next_column, rows):
    return 0 <= next_row < rows and 0 <= next_column < rows


def movement(direction, distance, start):
    row = start[0]
    col = start[1]

    if direction == 'up':
        return row - distance, col

    if direction == 'down':
        return row + distance, col

    if direction == 'left':
        return row, col - distance

    if direction == 'right':
        return row, col + distance


matrix = []

for i in range(5):
    matrix.append(input().strip().split(" "))

position = None
targets = []
hit_targets = []

for j in range(5):
    for k in range(5):
        if matrix[j][k] == 'x':
            targets.append([j, k])
        if matrix[j][k] == 'A':
            position = [j, k]

orders = int(input())
matrix[position[0]][position[1]] = '.'
is_complete = False
for order in range(orders):
    command = input().split(' ')
    turn = command[0]

    if turn == 'move':
        future_row, future_col = movement(command[1], int(command[2]), position)

        if is_inside(future_row, future_col, 5) and matrix[future_row][future_col] == '.':
            matrix[position[0]][position[1]] = '.'
            position = [future_row, future_col]

    elif turn == 'shoot':
        direction = command[1]

        if direction == 'up':
            for j in range(position[0] - 1, -1, -1):
                column = position[1]
                if [j, column] in targets:
                    targets.remove([j, column])
                    hit_targets.append([j, column])
                    matrix[j][column] = '.'
                    break
        elif direction == 'down':
            for k in range(position[0] + 1, 5):
                column = position[1]
                if [k, column] in targets:
                    targets.remove([k, column])
                    hit_targets.append([k, column])
                    matrix[k][column] = '.'
                    break
        elif direction == 'left':
            for l in range(position[1] - 1, -1, -1):
                row = position[0]
                if [row, l] in targets:
                    targets.remove([row, l])
                    hit_targets.append([row, l])
                    matrix[row][l] = '.'
                    break
        else:
            for z in range(position[1] + 1, 5):
                row = position[0]
                if [row, z] in targets:
                    targets.remove([row, z])
                    hit_targets.append([row, z])
                    matrix[row][z] = '.'
                    break

        if not targets:
            is_complete = True
            break

if is_complete:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {len(targets)} targets left.")

for i in hit_targets:
    print(i)

# def is_inside(next_row, next_column, rows):
#     return 0 <= next_row < rows and 0 <= next_column < rows
#
#
# def movement(direction, distance, start):
#     row = start[0]
#     col = start[1]
#
#     if direction == 'up':
#         return row - distance, col
#
#     if direction == 'down':
#         return row + distance, col
#
#     if direction == 'left':
#         return row, col - distance
#
#     if direction == 'right':
#         return row, col + distance
#
#
# matrix = []
#
# for i in range(5):
#     matrix.append(input().strip().split(" "))
#
# position = None
# targets = 0
# hit_targets = []
#
# for j in range(5):
#     for k in range(5):
#         if matrix[j][k] == 'x':
#             targets += 1
#         if matrix[j][k] == 'A':
#             position = [j, k]
#
# orders = int(input())
# is_complete = False
# for order in range(orders):
#     command = input().split(' ')
#     turn = command[0]
#
#     if turn == 'move':
#         future_row, future_col = movement(command[1], int(command[2]), position)
#
#         if is_inside(future_row, future_col, 5) and matrix[future_row][future_col] == '.':
#             matrix[position[0]][position[1]] = '.'
#             position = [future_row, future_col]
#
#     elif turn == 'shoot':
#         direction = command[1]
#         #This can be optimised to be a single function
#         if direction == 'up':
#             for j in range(position[0] - 1, -1, -1):
#                 column = position[1]
#                 if matrix[j][column] == 'x':
#                     targets -= 1
#                     hit_targets.append([j, column])
#                     matrix[j][column] = '.'
#                     break
#         elif direction == 'down':
#             for k in range(position[0] + 1, 5):
#                 column = position[1]
#                 if matrix[k][column] == 'x':
#                     targets -= 1
#                     hit_targets.append([k, column])
#                     matrix[k][column] = '.'
#                     break
#         elif direction == 'left':
#             for l in range(position[1] - 1, -1, -1):
#                 row = position[0]
#                 if matrix[row][l] == 'x':
#                     targets -= 1
#                     hit_targets.append([row, l])
#                     matrix[row][l] = '.'
#                     break
#         else:
#             for z in range(position[1] + 1, 5):
#                 row = position[0]
#                 if matrix[row][z] == 'x':
#                     targets -= 1
#                     hit_targets.append([row, z])
#                     matrix[row][z] = '.'
#                     break
#
#         if targets == 0:
#             is_complete = True
#             break
#
# if is_complete:
#     print(f"Training completed! All {len(hit_targets)} targets hit.")
# else:
#     print(f"Training not completed! {targets} targets left.")
#
# for i in hit_targets:
#     print(i)
