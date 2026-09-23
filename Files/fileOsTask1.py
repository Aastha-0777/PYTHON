import os

folderName = input("Enter the Folder's Name You want to Nevigate to : ")

if os.path.exists(f'./{folderName}') : 
    fileName = input("Enter the File Name You want to Delete : ")
    if os.path.exists(f'./{folderName}/{fileName}') : 
        os.remove(f'./{folderName}/{fileName}')
    else : 
        print(f'{fileName} Does not exit')
else :
    print(f'{folderName} does not exits')