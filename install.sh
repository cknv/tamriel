#!/bin/sh

python build.py

name="tamriel.sublime-package"
destination="$HOME/.config/sublime-text-3/Installed Packages/$name"

echo $name
echo $destination

rm "$destination"

sleep 2

mv "$name" "$destination"
