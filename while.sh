#!/bin/bash


# while [[ condition ]]; do
# 	#statements
# done



# counter=2

# while [[ counter -lt 10 ]]; do
# 	echo $counter
# 	(( counter ++ ))
# done



while true; do

	read -p "do you like this?" reply

	if [[ $reply == 'yes' ]]; then
		echo "Great"
		exit 0 

	elif [[ $reply == 'no' ]];then 
		echo "Sorry!"
		exit 0
	
	else
		echo "Try again"

	fi

done
