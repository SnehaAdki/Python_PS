
import os
print(os.getcwd()) #pwd output
print(os.listdir()) #it will list the directory

print(os.listdir("Collections"))

print(list(os.walk(os.getcwd()))) #it will give the directory tree

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current Path:",dirpath)
    print("Directories:",dirnames)
    print("Files:",filenames)
    print()

# 3 methods to delete a file
#os.unlink(path)
#os.rmdir(path)
#shutil.rmtree(path)
#pip install send2trash
# safer becz send to trash rather than removing directly