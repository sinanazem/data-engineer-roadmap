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

asama(){

	local name=${1:?You did not type anything}
	local age=${2}

	echo "Hello my name is ${name} and I am ${age} years old!"
}

asama 
