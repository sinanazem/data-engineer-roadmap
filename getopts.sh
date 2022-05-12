#!/bin/bash

# print_help(){
# 	echo "Usage: $0 [flags]"
# 	echo "Flags"
# 	echo "-h for help"
# 	echo "-b for male greeting"
# 	echo "-g for female greeting"
# }


# optstring=":hbg"

# while getopts ${optstring} options; do
# 	case ${options} in 
# 		b) 
# 			gender="boy";;
# 		g)
# 			gender="girl";;
# 		h)
# 			print_help 
# 			exit 0;;
# 		?)
# 			echo "Invalid option: -${OPTARG}"
# 			exit 1;;
# 		esac
# done

# if [[ -n ${gender} ]]; then
# 	echo "Hey ${gender}"
# else
# 	echo "Hey There!"

# fi





# echo $*

# shift

# echo $*



print_help(){

	echo "Usage: $0 [flags] <file_name>"
	echo "Flags:"
	echo "No flags for file listing"
	echo "-d to delete the file"
	echo "-e to empty the file"
	echo "-m <new_file_name> to rename the file."
	echo "-h for help."

}

command='ls -l'

optstring=':dem:h'

while getopts ${optstring} options; do
	
	case ${options} in 
		
		d)
			command='rm -f';;
		e) 
			command='cp /dev/null';;
		m)  
			new_file=${OPTARG}  command='mv';;

		h)
			print_help
			exit 0;;

		:)
			echo "-${OPTARG} requires an argument"; exit 1;;

		?)
			echo "Invalid option: -${OPTARG}."; exit 1;;

	esac
done

shift $(( ${OPTIND} - 1 ))


file_name=${1}

if [[ $# -ne 1 || ! -w ${file_name} ]]; then
	echo 'supply a writeable file to manipulate'
	exit 1
fi

if [[ -n ${new_file} ]]; then
	${command} ${file_name} $(dirname ${file_name})/${new_file}
else
	${command} ${file_name}
fi













































