class sequence_repeat:
    counter = 0

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if sequence_repeat.counter == self.number:
            raise StopIteration

        if len(self.sequence) < self.number:
            multiplier = self.number // len(self.sequence)
            sequence = (multiplier + 1) * self.sequence
        else:
            sequence = self.sequence

        to_append = sequence[sequence_repeat.counter]
        sequence_repeat.counter += 1

        return to_append


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')