#!/bin/bash
x=0
i=1
echo please enter a number
read num
while [ $i -le $num ]
do
s=`expr $i \* $i`
x=`expr $s + $x`
i=`expr $i + 1`
done

echo x=$x
