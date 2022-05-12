#!/bin/bash

#----------------------#
green='\033[92m'
red='\033[91m'
cyan='\033[96m'
blue='\033[94m'
yellow='\033[93m'
white='\033[0m'
magenta='\033[95m'
gray='033\[90m'
#----------------------#
clear

echo -e "${red}

 █████  ███████  █████  ███    ███  █████
██   ██ ██      ██   ██ ████  ████ ██   ██
███████ ███████ ███████ ██ ████ ██ ███████
██   ██      ██ ██   ██ ██  ██  ██ ██   ██
██   ██ ███████ ██   ██ ██      ██ ██   ██

"

echo -ne "${green} do you want to install pandas?"
read pandas

if [[ $pandas == y ]]; then
	sudo pip install pandas
elif [[ $pandas == n ]]; then
	echo -e "${red} install cancel!"
else
	echo -e "${yellow} i dont understand!"
fi