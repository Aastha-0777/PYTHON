import os
import shutil

#copy file
#src file must exists
#and at dest folder file must not exists..

# shutil.copy("demo.txt", "./Files/demoCopy.txt")

#move file
#src file must exists
#and at dest folder file must not exists..
# shutil.move("demo.txt", "./Files/demoMove.txt")

#copy folder
#src folder must exists
#and at dest folder folder must not exists..

# shutil.copytree("demo", "./Files/demoFolderCopy")

#move folder
#src folder must exists
#and at dest folder folder must not exists..

# shutil.move("demo", "./Files/demoFolderMove")

#lits all the items in a folder

items = os.listdir("Functions")
print(items)