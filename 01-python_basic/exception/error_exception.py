try:
#    11/0
    open("_.txt")
    print(num)
    print("1")

#except NameError:
#    print("Deal with NameError")

#except FileNotFoundError:
#    print("Deal with FileNotFoundError")
    
# use tuple to combine exception
except (NameError, FileNotFoundError) as e:
    print(e)
    print("Deal with Exception")

except Exception as ret:
    print("Catch another exception except NameError and FileNotFoundError")
    print(ret)
else :
    print("Excute with no exception")
finally :
    print("finally")

print("2")
