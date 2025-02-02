result = map(lambda number: number * 2, [1, 2, 3, 4])
print(list(result))




print([number * 2 for number in [1, 2, 3, 4]])





def double_numbers(list):
    double_list = []
    for num in list:
        double_list.append(num * 2)
    return double_list

print(double_numbers([1, 2, 3, 4]))