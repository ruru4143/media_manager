#!/usr/bin/python3.7
import sys
import os
import subprocess

path = sys.argv[1]

if len(sys.argv) != 2:
    print("Please provide one path as parameter (more than one parameter)")
    sys.exit()
elif not os.path.isdir(path):
    print("Please provide one path as parameter (parameter is not a path)")
    sys.exit()

print("Welcome to the show, rename, delete media manager")

feh_extensions = ["jpeg", "png", "jpg", "pnm", "tiff", "bmp", "mov"]
mpv_extensions = ["m4a", "3gp", "3g2", "mj2", "gif", "mp4"]

for file in [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]:  # get files only
    print(file)
    extension = file.split(".")[-1]
    if extension not in feh_extensions and extension not in mpv_extensions:
        continue
    elif extension in feh_extensions:
        process = subprocess.Popen(f"feh --full-screen {full_path_file}".split())

    elif extension in mpv_extensions:
        process = subprocess.Popen(f"mpv --fullscreen {full_path_file}".split())

    full_path_file = os.path.join(path, file)
    print(full_path_file)
    operator = input("do you want to do n(othing), d(elete), r(ename): ")

    if operator == "d":
        os.remove(full_path_file)
    elif operator == "r":
        new_name = input("                                                  new name:")
        os.rename(full_path_file, os.path.join(path, f"{new_name}.{extension}"))
    elif operator == "q":
        break
    else:
        print("do nothing")
