import os

# create testing files to rename
path = "test_batch_processing_rename_file"
os.chdir(path)
i = 1 
while i <= 5:
    filename = "status_of_my_teeth_" + str(i) + ".ig"
    f = open(filename, "w")
    f.close()
    i += 1

# rename the testing files

file_list = os.listdir()

file_list.sort()
print(file_list)

for filename in file_list:
    newfilename = "[Felix]-" + filename
    print(newfilename)
    os.rename(filename, newfilename)
