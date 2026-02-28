#19. Print all distinct values in a dictionary

data = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"},
        {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

values = set()
for d in data:
    for v in d.values():
        values.add(v)

print("Unique Values:", values)