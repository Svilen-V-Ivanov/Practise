from collections import deque

food_quantity = int(input())
orders = deque(int(x) for x in input().split(' '))
filtered_orders = orders.copy()

print(max(orders))

is_completed = False
for item in orders:

    if item <= food_quantity:
        food_quantity -= item
        filtered_orders.popleft()
        is_completed = True
    else:
        is_completed = False
        break

if is_completed:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(x) for x in filtered_orders)}")
