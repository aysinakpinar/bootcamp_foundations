def add_five(num):
    print(f"I've received {num}")
    num_after_adding = num + 5
    print(f"I've calculated {num} + 5 = {num_after_adding}")
    return num_after_adding

result1 = add_five(23)
result2 = add_five(result1)
result3 = add_five(result2)
print(result3)


