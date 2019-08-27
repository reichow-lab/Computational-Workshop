#!/bin/bash

n=0

echo "How many input files are there?"
read num_files
echo "What is your starting digit (infile)?"
read b
echo "What is the file starter (infile)?"
read file_from_starter
echo "What is the file ender (infile)?"
read file_from_ender
echo "What is the file starter (outfile)?"
read file_to_starter
echo "What is the file ender (outfile)?"
read file_to_ender
echo "What is your starting digit (outfile)?"
read c

while [ $n -lt $num_files ]
do

	printf -v num_b '%04d' $b
	printf -v num_c '%04d' $c

	from="$file_from_starter$num_b$file_from_ender"
	to="$file_to_starter$num_c$file_to_ender"

	mv $from $to

	((n++))
	((c++))
	((b++))
done
