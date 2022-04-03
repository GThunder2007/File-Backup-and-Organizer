import os
import shutil

source = input("Enter source folder name: ")
destination = input("Enter folder destination: ")

source = source + "/"
destination = destination + "/"

files = os.listdir(source)
for file in files:
    shutil.copy((source + file), destination)
