n, m = (int(x) for x in input().split(" "))
set_n = set()
set_m = set()
numbers_dict = {}
elements = []

for i in range(n):
    set_n.add(input())

for i in range(m):
    set_m.add(input())

joined = set_n.intersection(set_m)

for i in joined:
    print(i)
