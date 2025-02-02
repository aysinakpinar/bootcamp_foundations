passwords = [
    {"service": "takeway", "password": "asdf", "added_on": "21/03/22"},
    {"service": "acebook", "password": "password123", "added_on": "22/03/22"},
    {"service": "makersbnb", "password": "qwerty789", "added_on": "22/03/22"}
]
#1 for loop
# def added_on_21_03_22(passwords):
#     for dict in passwords:
#         if dict["added_on"] == "21/03/22":
#             print(dict["added_on"])
#             return True
#     return False

# print(added_on_21_03_22(passwords))


#2 filter-function
# def added_on_21_03_22(dict):
#     return dict["added_on"] == "21/03/22"

# def is_added_on_21_03_22(passwords):
#     return len(list(filter(added_on_21_03_22, passwords))) != 0

# print(is_added_on_21_03_22(passwords))


#3
# def is_added_on_21_03_22(passwords):
#     return list(filter(lambda dict: dict["added_on"] == "21/03/22", passwords)) != []

# print(is_added_on_21_03_22(passwords))


#4
# def is_added_on_21_03_22(passwords):
#     return len([dict for dict in passwords if dict["added_on"] == "21/03/22"]) != 0

# print(is_added_on_21_03_22(passwords))



#1 for loop
# def list_of_22_03_22(passwords):
#     final_list = []
#     for dict in passwords:
#         if dict["added_on"] == "22/03/22":
#             final_list.append(dict)
#     return final_list

#2 filter-function
# print(list_of_22_03_22(passwords))

# def is_22_03_22(dict):
#     return dict["added_on"] == "22/03/22"

# def is_22_03_22_in(passwors):
#     return list(filter(is_22_03_22, passwords))

# print(is_22_03_22_in(passwords))


#3 filter-lambda
# def is_22_03_22_in(passwords):
#     return list(filter(lambda dict: dict["added_on"] == "22/03/22", passwords))

# print(is_22_03_22_in(passwords))


#4 list comprehension
# def is_22_03_22_in(passwords):
#     return list(dict for dict in passwords if dict["added_on"] == "22/03/22")

# print(is_22_03_22_in(passwords))