rows, columns = (int(x) for x in input().split(" "))
matrix = []

for i in range(rows):
    matrix.append(input().split(" "))

count = 0

for i in range(rows - 1):
    for j in range(columns - 1):
        if (matrix[i][j] == matrix[i + 1][j]
                and matrix[i][j] == matrix[i][j + 1]
                and matrix[i][j] == matrix[i + 1][j + 1]):
            count += 1

print(count)
