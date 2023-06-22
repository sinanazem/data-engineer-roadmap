#!/bin/bash


names="Sina Ali Reza Mehrad Sara Nazanin Maral"

# for name in $names;do
# 	if [[ $name == Mehrad ]]; then
# 		continue
# 	fi
# 	echo $name

# done



for name in $names;do
	if [[ $name == "Mehrad" ]]; then
		break
	fi
	echo $name
done