BK="ad-bk.txt"
exit=0
while [ $exit -ne 1 ]
do
	echo "Do you want to add, list, find, delete, or exit?"
	read resp

	if [ "$resp" = "list" ]
	then
		echo "Line Number:   Name  ;  Phone Number"
		nl --number-separator=":    " $BK
		sort -o fn.txt ad-bk.txt 
                cp fn.txt ad-bk.txt
	elif [ "$resp" = "find" ]
	then
		echo -n "What person are you seeking?"
        	read fnd
		echo "Name ; Phone number"
        	grep -i $fnd $BK
		sort -o fn.txt ad-bk.txt 
                cp fn.txt ad-bk.txt
	elif [ "$resp" = "del" ]
	then
		echo -n "Which name should I delete: "
        	read peru
		sed -e  "/$peru/d" fn.txt | tee $BK
		sort -o fn.txt ad-bk.txt | cat fn.txt 
                cp fn.txt ad-bk.txt
	elif [ "$resp" = "exit" ]
	then
		exit=1
	elif [ "$resp" = "add" ]
	then
		echo -n "Name of person: " 
        	read peru
		echo -n "Phone number: "
        	read phone
		echo "Are you sure? (y/n)"
		read res
		if [ "$res" = "y" ]
		then
			echo "$peru ; $phone" >>$BK
		else
			echo "It has not been appended!"
		fi
		sort -o fn.txt ad-bk.txt
                cp fn.txt ad-bk.txt
	else
		echo "Error in command. Try again."
	fi
done
exit 0
