#!/usr/bin/python3.7
import sys
import sh

if len(sys.argv) != 1:
    print("Please provide one path as parameter")

path = sys.argv[1]

print("Welcome to the show, rename, delete media manager")

feh_extensions = ["jpeg", "png", "jpg", "pnm", "tiff", "bmp", "mov"]
mpv_extensions = ["m4a", "3gp", "3g2", "mj2", "gif", "mp4"]

for file in str(sh.find(path, "-maxdepth", "1", "-type", "f")).split("\n"):
    extension = file.split(".")[-1]
    if extension not in feh_extensions and extension not in mpv_extensions:
        continue
    elif extension in feh_extensions:
        sh.feh("--full-screen", file)
    elif extension in mpv_extensions:
        sh.mpv("--fullscreen", file)

    print(path)
    operator = input("do you want to do n(othing), d(elete), r(ename): ")

    if operator == "d":
        sh.rm(file)
    elif operator == "r":
        new_name = input("                                                  new name:")
        sh.mv(file, path+new_name+"."+file.split(".")[-1])
    elif operator == "q":
        break
    else:
        print("do nothing")
