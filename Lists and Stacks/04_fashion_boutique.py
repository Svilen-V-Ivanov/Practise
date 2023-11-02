from collections import deque

clothes_box = deque(int(x) for x in input().split(' '))
rack_capacity = int(input())
current_capacity = rack_capacity
needed_racks = 0

while clothes_box:
    cloth = clothes_box.pop()

    if cloth > current_capacity:
        needed_racks += 1
        current_capacity = rack_capacity
        clothes_box.append(cloth)
    elif cloth == current_capacity:
        needed_racks += 1
        current_capacity = rack_capacity
    elif cloth < current_capacity and not clothes_box:
        needed_racks += 1
        current_capacity -= cloth
    else:
        current_capacity -= cloth

print(needed_racks)
