def concatenate(*args, **kwargs):
    string = ''.join(args)

    for key, value in kwargs.items():
        #This check isn't needed, but it's good to have imo
        if key in string:
            string = string.replace(key, value)

    return string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
