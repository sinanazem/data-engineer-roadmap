#!/bin/bash

#name=${1}

#echo ${name:2:5}


#sentance=${1}

#echo ${sentance//bad/good}

#name=${1}

if [[ ${#*} -ne 1 ]]; then
	echo "we need exacly on parameter"
	exit 1
fi

name=${1}

if [[ ${#name} -ne 3 ]]; then
	echo 'name exacly 3 lett'
	exit 2
fi

echo "Hey ${name}"
