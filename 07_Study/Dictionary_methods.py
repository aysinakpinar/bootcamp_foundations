tourny_dict = {"Dan":2, "Wolfgang":14, "June":43, "Tany":32, "Sharon": 8}
scores = [1, 3, 4, 3, 5]
count = 0
for x in tourny_dict:
    tourny_dict[x] += scores[count]
    count += 1

print(tourny_dict)

tourny_dict = {'Dan': 3, 'Wolfgang': 17, 'June': 47, 'Tany': 35, 'Sharon': 13}
scores = [7, 3, 6, 2, 1]

update_dict_comp = {key: value + scores[list(tourny_dict.keys()).index(key)] for (key, value) in tourny_dict.items()}
tourny_dict.update(update_dict_comp)

print(tourny_dict)