filename = input("which file do you want to bake up?")

# find the suffix of the filename
pos = filename.rfind(".")

# construct the file name for backup
backup_filename = filename[:pos] + ".bak"

with open(filename, "r", encoding="utf-8") as old_file:
    with open(backup_filename, "w", encoding="utf-8") as new_file:
        content = old_file.read()
        new_file.write(content)
