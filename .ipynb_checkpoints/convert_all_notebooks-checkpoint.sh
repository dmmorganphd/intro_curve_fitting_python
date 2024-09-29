#!/usr/bin/bash

files=`ls -al *.ipynb`

for file in $files; do 
    echo $file
done