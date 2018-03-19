listtemp = [ "apple", "python", "elephant", "cat", "zbra", "aaaaaaaa"]

# get the first largest string in list
print(max(listtemp, key=len))

print(max(listtemp, key=lambda s: (len(s), s)))


