import os

#create testing files to rename
path = "test_batch_processing_rename_file"
os.chdir(path)
i = 1 
while i <= 5:
    filename = "statusofmyteeth_" + str(i) + ".ig"
    f = open(filename, "w")
    f.close()
    i+=1

# rename the testing files

filelist = os.listdir()

filelist.sort()
print(filelist)

for filename in filelist:
    newfilename = "[Felix]-" + filename
    print(newfilename)
    os.rename(filename, newfilename)
