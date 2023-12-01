class countdown_iterator:
    counter = 0

    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if countdown_iterator.counter > int(self.count):
            raise StopIteration

        result_to_append = self.count - countdown_iterator.counter
        countdown_iterator.counter += 1

        return result_to_append


# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")