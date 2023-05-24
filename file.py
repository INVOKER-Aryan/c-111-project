import os
import shutil
from_dir = 'C:/Users/AMD RYZEN/Downloads'
to_dir = 'C:/Users/AMD RYZEN/Desktop'
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension == "":
        continue
    if extension in [".doc",".pdf",".exe",".csv",".xls"]:
        path1 = from_dir + "/"+ file_name
        path2 = to_dir +"/"+ "document_files"
        path3 = to_dir +"/"+ "document_files"+"/"+file_name
        print("soures path is...",path1)
        print("destination folder path is...",path2)
        print("destination file path is...",path3)
        if os.path.exists(path2):
            print("moving "+file_name+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving "+file_name+"...")
            shutil.move(path1,path3)