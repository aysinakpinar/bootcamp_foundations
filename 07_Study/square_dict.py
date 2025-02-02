square_dict = {}
for num in range(1,11):
    square_dict[num] = num * num

print(square_dict)


square_dict = {num: num * num for num in range(1, 11)}
print(square_dict)
for i in square_dict.items():
    print(i)


person = {"name" : "Jo", "age": 42, "height": 170}
for item in person:
    print(f"key value pair: {item} -> {person[item]}")
