class dictionary_iter:
    counter = 0

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __iter__(self):
        return self

    def __next__(self):
        if dictionary_iter.counter == len(self.dictionary):
            raise StopIteration
        keys = list(self.dictionary.keys())
        key_to_append = keys[dictionary_iter.counter]
        #value_to_append = self.dictionary[key_to_append]
        result_to_append = [key_to_append, self.dictionary[key_to_append]]
        dictionary_iter.counter += 1
        return tuple(result_to_append)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)