#!/bin/bash

add(){
	
	x=${1}
	y=${2}

	local sum=$(( x+y ))

	echo $sum
}

result=$(add 3 4)

echo $result