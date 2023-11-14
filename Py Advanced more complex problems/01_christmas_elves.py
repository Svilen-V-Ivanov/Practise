from collections import deque

elves = deque(int(x) for x in input().split(" "))
boxes = [int(x) for x in input().split(" ")]
toys_made = 0
cycles = 0
spent_energy = 0

while elves and boxes:
    elf = elves.popleft()
    box = boxes.pop()

    if elf < 5:
        boxes.append(box)
        continue

    cycles += 1

    if cycles % 5 == 0 and cycles % 3 == 0:
        if box * 2 <= elf:
            spent_energy += box * 2
            elf -= box * 2
            elves.append(elf)
        else:
            elves.append(elf * 2)
            boxes.append(box)
    elif cycles % 5 == 0:
        if box <= elf:
            spent_energy += box
            elf -= box
            elves.append(elf)
        else:
            elves.append(elf * 2)
            boxes.append(box)
    elif cycles % 3 == 0:
        if box * 2 <= elf:
            spent_energy += box * 2
            elf -= box * 2
            toys_made += 2
            elves.append(elf + 1)
        else:
            elves.append(elf * 2)
            boxes.append(box)
    else:
        if box <= elf:
            spent_energy += box
            elf -= box
            toys_made += 1
            elves.append(elf + 1)
        else:
            elves.append(elf * 2)
            boxes.append(box)

print(f"Toys: {toys_made}")
print(f"Energy: {spent_energy}")
if elves:
    print(f"Elves left: {', '.join(str(x) for x in elves)}")
if boxes:
    print(f"Boxes left: {', '.join(str(x) for x in boxes)}")
