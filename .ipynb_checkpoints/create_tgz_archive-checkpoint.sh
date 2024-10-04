#!/usr/bin/bash

wd=`pwd`
parentdir="$(dirname "$wd")"
cd $parentdir
if [ $? != 0 ]; then
        echo "problem changing to parent directory"
        exit
fi

IFS='/'
read -ra newarr <<< $wd
tfn=${newarr[-1+${#newarr[@]}]}".tgz"
tar --exclude="*git*" -zcvf $tfn ${newarr[-1+${#newarr[@]}]}