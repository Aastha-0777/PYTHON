import os
import shutil

folderName = input("Enter the Folder's Name You want to Nevigate to : ")

if os.path.exists(f'./{folderName}') : 
    subFolder = input("Enter the SubFolder Name You want to delete tree of : ")
    if os.path.exists(f'./{folderName}/{subFolder}') : 
        shutil.rmtree(f'./{folderName}/{subFolder}')
    else : 
        print(f'./{folderName}/{subFolder} Does not exit')
else : 
    print(f'./{folderName} does not exit')
