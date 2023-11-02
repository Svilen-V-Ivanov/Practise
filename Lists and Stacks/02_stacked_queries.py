numbers = int(input())
stack = []

for i in range(numbers):
    command = input().split(' ')
    order = int(command[0])

    if order == 1:
        stack.append(int(command[1]))
    elif order == 2:
        if stack:
            stack.pop()
    elif order == 3 and stack:
        print(max(stack))
    elif order == 4 and stack:
        print(min(stack))

reversed_stack = []

while stack:
    reversed_stack.append(str(stack.pop()))

print(", ".join(reversed_stack))
