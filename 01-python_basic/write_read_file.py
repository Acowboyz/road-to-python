f = open("read_write_file.txt", "w")

f.write("test !!!! \n")
f.write("test !!!! \n")
f.write("test !!!! \n")
f.write("test !!!! \n")

f.close()

f = open("read_write_file.txt","r")

print(f.read())

f.close()
