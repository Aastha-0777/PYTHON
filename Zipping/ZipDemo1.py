import zipfile
import datetime

with zipfile.ZipFile(f'{datetime.date.today()}.zip', 'w') as z : 
    z.write("notes.txt")
    z.write("Files/demo2.txt")

print('Zip File Created...')