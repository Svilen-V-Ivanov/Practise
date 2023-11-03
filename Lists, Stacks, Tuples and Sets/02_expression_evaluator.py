def calculate_result(a, b, operator):
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/':
        return a // b


sequence = input().split(' ')
result = int(sequence.pop(0))
num_sequence = []


while sequence:

    value = sequence.pop(0)

    if value not in '+-*/':
        num_sequence.append(int(value))
    else:
        for num in num_sequence:
            result = calculate_result(result, num, value)
            num_sequence = []

print(result)
