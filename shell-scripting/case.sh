#!/bin/bash

name=${1}

case $name in 
	jack)
	    echo 'Hello Jack';;

	mark)
		echo 'Hello Mark';;
	amir)
		echo 'Hi Amir';;
	*)
		echo "Unknown"
esac

