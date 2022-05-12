#!/bin/bash

check_integer(){
	
	if [[ $# -ne 1 ]]; then
		echo "Need exactly one argument, eciting..."
		exit 1
	fi

	if [[ $1 =~ ^[[:digit:]]+$ ]];then
		echo "Integer"

	else
		echo "Non Integer"

	fi
}

check_integer ${1}
