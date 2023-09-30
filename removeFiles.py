import time
import shutil
import os

folder = input("Path: ")
days = 30
time_in_seconds = 0
current_time = time.time()
print(os.path.exists(folder))
os.chdir(os.path.join(os.getcwd(),folder))
listoffiles = os.listdir
listoffiles1 = os.walk(folder)

for path,subdirs,files in os.walk(folder) :
    for name in files:
        fileLocation = os.path.join(path,name)
        fileTime = int(os.stat(fileLocation).st_mtime)
        dif = int(current_time-time_in_seconds)
        if (fileTime<dif) :
            print("Delete",name)

        if(os.path.isfile(fileLocation)):
            os.remove(fileLocation)

        elif(os.pathisdir(fileLocation)) :
            shutil.rmtree(fileLocation)