# If a line is commented out, it does not work!

numbers = [4, 6, 10, 99]

print(numbers[1]) #index notation (list)

user = {
    #key: value
    "name": "Spongebob",
    "home": "pineapple",
    "num_of_pets": 1,
    "favorite_numbers": [7, 3, 9, 2]
}

print(user)
print(user["home"]) #key notation (dictionary)
# print(user[1])
print(user["favorite_numbers"][0])
# print(user.favorite_numbers) #dot notation (dictionary)
user["friend"] = "Patrick"
user["favorite_numbers"].append(5)
print(user)
# print(user["workplace"])

users = [
    {"name": "Pearl", "favorite_numbers": [12, 13, 14]},
    {"name": "Mr. Krabs"},
    {"name": "Squidward"},
    {"name": "Plankton"},
    {"name": "Karen"}
]
print(users)
print(users[3])
print(users[3]["name"])
# # print(users[3].value)
# # print(users["name"])
print(users[0]["favorite_numbers"][2])
users.append({"name": "Sandy"})
print(users)

for user in users:
    print(user)