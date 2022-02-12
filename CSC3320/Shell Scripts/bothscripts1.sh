echo "Enter a number"
read val
echo "Since the factorial is only implemented for integers, it can only be accurate for a maximum value of 20, as the other numbers will overflow and cause innacuracies."
gcc -o ~/factorial ~/factorial.c
./factorial <<< $val

gcc -o bitwiseopp bitwiseopp.c 
./bitwiseopp <<< $val
