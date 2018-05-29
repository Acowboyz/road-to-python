with open("read_write_file.txt", "w", encoding="utf-8") as f:
    f.write("test !!!! \n")
    f.write("test !!!! \n")
    f.write("test !!!! \n")
    f.write("test !!!! \n")

with open("read_write_file.txt", "r", encoding="utf-8") as f:
    print(f.read())

