number = int(input())
elements = set()

for i in range(number):
    molecules = input().split(" ")
    for piece in molecules:
        elements.add(piece)

for j in elements:
    print(j)
