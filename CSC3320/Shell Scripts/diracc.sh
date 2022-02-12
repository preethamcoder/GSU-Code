#!/bin/bash
echo Enter the number of days
read days
find ~ -iname "*" -atime +$days -type f|zip compressedfile -@
