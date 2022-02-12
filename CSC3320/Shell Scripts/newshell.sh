#!/bin/bash
echo enter the command
read com \c
echo `man $com` > data.txt
cat data.txt
