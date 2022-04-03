from importlib.resources import path
import os
import shutil

Path = input("Enter the folder path: ")
files = os.listdir(path)
for file in files:
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == "":
        continue
    if os.path.exists(path + "/" + ext):
        shutil.move(path + "/" + file, path + "/" + ext + "/" + file)
    else:
        os.makedirs(path + "/" + ext)
        shutil.move(path + "/" + file, path + "/" + ext + "/" + file)
