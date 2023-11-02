text = input()
letter_dict = {

}

for letter in text:
    if letter not in letter_dict.keys():
        letter_dict[letter] = 1
    else:
        letter_dict[letter] += 1

sorted_letters = dict(sorted(letter_dict.items()))

for key, value in sorted_letters.items():
    print(f"{key}: {value} time/s")
