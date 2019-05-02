#!/bin/bash

path=$1

test -d $path
if [[ $? -ne 0 ]]; then # test if param is a path
  echo "Please provide one path as parameter (parameter is not a path)"
  exit
elif [[ $# -ne 1 ]]; then
  echo "Please provide one path as parameter (more than one parameter)"
  exit
fi

echo "Welcome to the show, rename, delete media manager"

image_extensions="jpeg png jpg pnm tiff bmp mov"
video_extensions="m4a 3gp 3g2 mj2 gif mp4"

for file in $(find "$path" -maxdepth 1 -type f | egrep "(\.jpg)|(\.jpeg)|(\.png)|(\.pnm)|(\.tiff)|(\.bmp)|(\.mov)|(\.mp4)|(\.m4a)|(\.3gp)|(\.3g2)|(\.mj2)|(\.gif)"); do  
  if [[ $image_extensions == *"${file#*.}"* ]]; then
    feh --full-screen $file
  elif [[ $video_extensions == *"${file#*.}"* ]]; then
    mpv --fullscreen $file
  else
    echo "failing..."
  fi
  
  echo $file
  echo -n "do you want to do n(othing), d(elete), r(ename): "
  read operator
  
  if [[ "$operator" == "d" ]]; then
    rm $file
  elif [[ "$operator" == "r" ]]; then
    echo -n "                                                 		new name: "
    read new_name
	mv $file $(echo $path/$new_name\.${file#*.})
  else
    echo "do nothing"
  fi
done