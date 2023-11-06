def movement(position, comm, row, col):
    if comm == 'up' and position[0] > 0:
        position[0] -= 1

    if comm == 'down' and position[0] < row - 1:
        position[0] += 1

    if comm == 'left' and position[1] > 0:
        position[1] -= 1

    if comm == 'right' and position[1] < col - 1:
        position[1] += 1

    return position


rows = int(input())
commands = input().split(" ")
matrix = []
coal = []
cols = 0
miner_position = None
exit_position = None
collected_coal = 0

for i in range(rows):
    row = input().split(" ")
    cols = len(row)
    matrix.append(row)

    for j in range(len(row)):
        if row[j] == 's':
            miner_position = [i, j]
        if row[j] == 'e':
            exit_position = [i, j]
        if row[j] == 'c':
            coal.append([i, j])

is_over = False
all_coal = len(coal)

for order in commands:
    old_position = miner_position.copy()
    miner_position = movement(miner_position, order, rows, cols)

    if miner_position == exit_position:
        print(f"Game over! ({', '.join(str(x) for x in miner_position)})")
        is_over = True
        break

    if miner_position in coal:
        collected_coal += 1
        coal.remove(miner_position)

    if not coal:
        print(f"You collected all coal! ({', '.join(str(x) for x in miner_position)})")
        break

    if old_position[0] == miner_position[0] and old_position[1] == miner_position[1]:
        pass
    else:
        old_x = old_position[0]
        old_y = old_position[1]
        matrix[old_x][old_y] = '*'

    #to keep track of miner
    miner_x = miner_position[0]
    miner_y = miner_position[1]
    matrix[miner_x][miner_y] = 'm'

if coal and not is_over:
    print(f"{all_coal - collected_coal} pieces of coal left. ({', '.join(str(x) for x in miner_position)})")