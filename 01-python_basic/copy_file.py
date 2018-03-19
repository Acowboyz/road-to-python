filename = input("which file do you want to bake up?")

#find the suffix of the filename
pos = filename.rfind(".")

bakfilename = filename[:pos] + ".bak"

oldfile = open(filename,"r")
newfile = open(bakfilename,"w")

content = oldfile.read()

newfile.write(content)

oldfile.close()
newfile.close()
