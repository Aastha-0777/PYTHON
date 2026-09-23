import os
import shutil

#To check whether a file exits or not
# res = os.path.exists("notes.txt") -> False
res = os.path.exists("./Files/notes.txt")
print(res)

#To rename a file
#To rename a file we first have to check whether it exits or not

if os.path.exists("./Files/task.txt") : 
    os.rename("./Files/task.txt", "task_demo.txt")
else : 
    print("File Not Found..")

#To delete a file
#To delete a file we first have to check whether it exits or not

if os.path.exists("./Files/task.txt") : 
    os.remove("./Files/task.txt")
else : 
    print("File Not Found..")

#to create a folder it is same as linux mkdir but if it already exits than it trows exception

if not os.path.exists("./Files/task") : 
    os.mkdir("./Files/task")
else : 
    print("Folder already exits..")

#to delete a folder it is same as linux rmdir but if it does not exits than it trows exception

if os.path.exists("./Files/task") : 
    os.rmdir("./Files/task")
else : 
    print("Folder does not exits..")


#to delete a folder that is not empty then you have to use shutil.rmtree i.e remove tree
#if folder does not exits than it trows exception
#it will delete the entier folder with everything inside that folder

if os.path.exists("C:/PYTHON/Files/shutilDemo") : 
    shutil.rmtree("C:/PYTHON/Files/shutilDemo")
else : 
    print("Folder does not exits..")