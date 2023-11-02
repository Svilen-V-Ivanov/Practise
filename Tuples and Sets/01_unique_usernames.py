number = int(input())
names = []

for i in range(number):
    name = input()
    names.append(name)

set_names = set(names)
for name in set_names:
    print(name)