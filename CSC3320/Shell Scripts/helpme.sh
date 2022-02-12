#!/bin/bash
echo Enter the command you want to search
read com \c
x=1
condition="$(grep -i ^$com\( mandatabase.txt | wc -l)" 
if [ $condition -ge $x ]
then
#com2=$com"(1)"
#echo "$(grep ^${com2^^}.*${com2^^} mandatabase.txt)"
#echo "$(sed -n '/"NAME"/,/"${com2^^}"$/p' mandatabase.txt)"
#$echo `man $com`
#echo "$(awk '/^${com2^^}/,/${com2^^}$/' mandatabase.txt)"
n="0"
while read line; do
if [[ $line == ${com^^}"("* ]]
then
  echo "$line"
  n="1"
elif [[ "$n" -eq "1" && $line != *${com^^}"(1)" ]]
then
  echo "$line"
elif [[ "$n" -eq "1" && $line == *${com^^}"(1)" ]]
then
  echo "$line"
  n="0"
fi
done < mandatabase.txt
else
	echo sorry, I cannot help you
fi
