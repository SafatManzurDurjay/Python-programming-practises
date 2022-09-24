numbers = [2, 2, 3, 9, 7, 5, 5, 6, 8, 6, 4, 3, 1, 5, 9, 5, 6, 4]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
