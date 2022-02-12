#!/bin/bash
echo "Type in the word you want to search"
read word
count="$(grep -wi $word myexamfile.txt | wc -l)"
echo "$word occured $count times in the file."
