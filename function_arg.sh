#!/bin/bash

# show(){
# 	name=${1}
# 	age=${2}

# 	echo "your name is ${name} and you are ${age} years old"
# }

# show $1 $2

green='\033[92m'
red='\033[91m'
cyan='\033[96m'
blue='\033[94m'
yellow='\033[93m'
white='\033[0m'
magenta='\033[95m'
gray='033\[90m'

colorful(){
	
	if [[ $# -ne 2 ]]; then
		echo "colorful needs 2 arguments"
		exit 1
	fi
	
	local string=${1}
	local color=${2}

	if [[ color == "red" ]]; then
		local color_code='\033[91m'
	
	elif [[ color == "blue" ]]; then
		local color_code='\033[94m'

	
	elif [[ color == "green" ]]; then 
		local color_code='\033[92m'

	else 
		local color_code='\033[95m'

	fi
	
	echo -e "${color_code}${string}"
}

#colorful "This is Red" "red"
#colorful "This is yellow" "yellow"
colorful "This is green" "green"
# colorful "This is blue" "blue"