def age_assignment(*args, **kwargs):
    people = {}

    for person in args:
        for key, value in kwargs.items():
            if person[0] == key:
                people[person] = value

    return "\n".join(f"{name} is {age} years old." for name, age in sorted(people.items(), key=lambda x: x[0]))


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))