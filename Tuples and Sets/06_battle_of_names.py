number = int(input())
odd = set()
even = set()
end_set = set()

for i in range(1, number + 1):
    name = input()

    local_sum = sum(ord(x) for x in name) // i

    if local_sum % 2 == 0:
        even.add(local_sum)
    else:
        odd.add(local_sum)

if sum(odd) == sum(even):
    end_set = odd.union(even)
elif sum(odd) > sum(even):
    end_set = odd.difference(even)
else:
    end_set = odd.symmetric_difference(even)

print(', '.join(str(x) for x in end_set))

