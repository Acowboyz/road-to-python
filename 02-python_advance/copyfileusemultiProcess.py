from multiprocessing import Pool, Manager
import os

def copyFileTask(name, oldFolderName, newFolderName, queue):

    fr = open(oldFolderName + "/" + name)
    fw = open(newFolderName + "/" + name, "w")

    content = fr.read()
    fw.write(content)
    
    fr.close()
    fw.close()

    queue.put(name) 
    

def main():
    # 0. input the folder name that user wants to copy 
    oldFolderName = input("please enter the folder name that you want to copy:")

    # 1. make new directory
    newFolderName = oldFolderName + "-bak"
    #print(newFolderName)
    os.mkdir(newFolderName)

    # 2. get the file name from old directory
    oldFileNames = os.listdir(oldFolderName)
    #print(oldFileNames)

    # 3. use multiprogress to copy old files to new folder
    pool  = Pool(5)
    queue = Manager().Queue()

    for name in oldFileNames:
        pool.apply_async(copyFileTask, args=(name, oldFolderName, newFolderName, queue))

    num = 0
    allNum = len(oldFileNames)
    while num < allNum:
        queue.get()
        num += 1
        copyRate = num/allNum
        print("\rcopy : %.2f%%"%(copyRate*100), end="")

    print("\ncopy complete !!!")
    #pool.close()
    #pool.join()

if __name__ == "__main__":
    main()
