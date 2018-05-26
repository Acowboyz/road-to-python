l = [
    {"name": "felix", "age": 18},
    {"name": "melissa", "age": 17},
    {"name": "van", "age": 16}
]

# sort by the first letter of name
l.sort(key=lambda x: x["name"])

print(l)

l.sort(key=lambda x: x["age"])

print(l)