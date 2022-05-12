#!/bin/bash


if [[ $# -ne 3 ]]; then
	echo "bad usage"
	echo "usage: Mongard10.sh <directory> <file_name> <content>"
	exit 1

fi

directory=${1}
file_name=${2}
content=${3}
path=${directory}/${file_name}



if [[ ! -d ${directory} ]]; then
	mkdir ${directory} || { echo 'Cant create directory'; exit 1; }

fi

if [[ ! -f ${path} ]]; then
	touch ${path} || { echo 'Cant create file'; exit 1; }
fi


echo ${content} > ${path}