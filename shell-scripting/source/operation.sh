#!/bin/bash

add(){

	local x=${1}
	local y=${2}

	local sum=$(( x+y ))
	echo $sum
}


sub(){

	local x=${1}
	local y=${2}

	local sub=$(( x-y ))
	echo $sub
}



