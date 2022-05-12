#!/bin/bash


number=10


until [[ number -gt 20 ]]; do
	echo $number
	(( number ++ ))
done