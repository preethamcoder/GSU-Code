#!/bin/bash
echo "Welcome to the Computer Science Society!"
#My name is Preetham Thelluri and my email is sthelluri1@student.gsu.edu
echo "Date is: `date`"
echo "Printing # of directories in /home:"
echo /home/*|wc -w
echo $PATH
echo $USER
echo $SHELL
echo "Printing the disk usage: "
echo `df`
echo "Please, could you loan me "$"25.00?"
echo "if x = 2, x * x = 4, x / 2 = 1"
echo "`ls *.sh | grep c`"
echo "Good Bye"
echo "Current Hour = `date +'%H'`"
