from collections import deque

chocolate = [int(x) for x in input().split(', ')]
milk_cups = deque(int(x) for x in input().split(', '))
total_milkshakes = 0
is_completed = False

while milk_cups and chocolate and total_milkshakes < 5:

    cup_of_milk = milk_cups.popleft()
    choco = chocolate.pop()

    if choco <= 0 and cup_of_milk <= 0:
        continue
    elif choco <= 0:
        milk_cups.appendleft(cup_of_milk)
    elif cup_of_milk <= 0:
        chocolate.append(choco)
    else:
        if cup_of_milk == choco:
            total_milkshakes += 1
        else:
            milk_cups.append(cup_of_milk)
            choco -= 5
            chocolate.append(choco)

    if total_milkshakes == 5:
        is_completed = True


if not is_completed:
    print('Not enough milkshakes.')
else:
    print("Great! You made all the chocolate milkshakes needed!")

if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join(str(x) for x in milk_cups)}")
else:
    print("Milk: empty")

# from collections import deque
#
# chocolate_packages = [int(x) for x in input().split(', ')]
# milk_cups = deque(int(x) for x in input().split(', '))
#
# milkshakes = 0
#
# while chocolate_packages and milk_cups and milkshakes < 5:
#     chocolate = chocolate_packages.pop()
#     milk = milk_cups.popleft()
#
#     if chocolate <= 0  and milk <= 0:
#         continue
#     if chocolate <= 0:
#         milk_cups.appendleft(milk)
#         continue
#     if milk <= 0:
#         chocolate_packages.append(chocolate)
#         continue
#
#     if chocolate == milk:
#         milkshakes += 1
#     else:
#         chocolate_packages.append(chocolate - 5)
#         milk_cups.append(milk)
#
# if milkshakes == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
#
# if chocolate_packages:
#     print(f"Chocolate: {', '.join(str(x) for x in chocolate_packages)}")
# else:
#     print(f"Chocolate: empty")
#
# if milk_cups:
#     print(f"Milk: {', '.join(str(x) for x in milk_cups)}")
# else:
#     print(f"Milk: empty")