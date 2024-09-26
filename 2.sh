#!/usr/bin/bash

IFS='/'
read -ra newarr <<< `pwd`

echo "string read"
echo ${#newarr[@]}
# Print each value of the array by using
# the loop
for val in "${newarr[@]}";
do
	 echo "$val"
 done

echo "there are "${#newarr[@]}" elements in newarr and the last element is: "${newarr[-1+${#newarr[@]}]}
