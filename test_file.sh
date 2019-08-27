echo "How many files do you want to create?"
read num_files

echo "What is the prefix of your file?"
read prefix

echo "What is the ending of your file?"
read suffix

echo "What is the starting digit of your files?"
read init_digit

n=0

while [ $n -lt $num_files ]
do

printf -v digit '%04s' $init_digit

new_file="$prefix$digit$suffix"

touch $new_file

((n++))
((init_digit++))

done

