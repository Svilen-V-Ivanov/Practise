def calculate_sequence(*args):
    positive_sequence = []
    negative_sequence = []

    for num in args:
        if num < 0:
            negative_sequence.append(num)
        else:
            positive_sequence.append(num)

    print(sum(negative_sequence))
    print(sum(positive_sequence))

    if abs(sum(negative_sequence)) > sum(positive_sequence):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
calculate_sequence(*numbers)
