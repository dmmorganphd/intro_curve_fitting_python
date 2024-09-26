#!/usr/bin/bash

IFS='/'
read -ra newarr <<< `pwd`

# echo "there are "${#newarr[@]}" elements in newarr and the last element is: "${newarr[-1+${#newarr[@]}]}

datestamp=`date +%s`
nfn="..//"${newarr[-1+${#newarr[@]}]}

echo $nfn
