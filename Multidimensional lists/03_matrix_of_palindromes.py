rows, columns = (int(x) for x in input().split(" "))
matrix = []

letters = 'abcdefghijklmnopqrstuvwxyz'

for i in range(rows):
    matrix.append([])
    for j in range(columns):
        matrix[i].append(f"{letters[i]}{letters[j + i]}{letters[i]}")

for i in range(rows):
    print(" ".join(str(x) for x in matrix[i]))
