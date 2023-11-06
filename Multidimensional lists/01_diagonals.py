size = int(input())
matrix = []
main_diagonal = []
secondary_diagonal = []

for i in range(size):
    matrix.append([int(x) for x in input().split(", ")])

for j in range(size):
    main_diagonal.append(matrix[j][j])
    secondary_diagonal.append(matrix[j][size - 1 - j])

print(f"Primary diagonal: {', '.join(str(x) for x in main_diagonal)}. Sum: {sum(main_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
