#!/bin/bash


names=(amir jack kevin mark)

echo ${names[0]}

# get fourth item from arrays
echo ${names[3]}

# unpack elements from array
echo ${names[@]}

#get indext of element in array
echo ${!names[@]}

# length of array
echo ${#names[@]}

# loop in array

for item in ${names[@]}; do
	echo $item
done


#append and extend in arrays

names+=(sina elnaz)
echo ${names[@]}

# remove in arrays

unset names[1]
echo ${names[@]}

