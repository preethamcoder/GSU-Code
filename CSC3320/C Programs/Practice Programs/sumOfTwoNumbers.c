#include <stdio.h>
int sumf(int a, int b);
int main(){
int num1 = 12, num2 = 13;
printf("The sum is: %d", sumf(num1, num2));
return 0;
}
int sumf(int a, int b){
	return(a+b);
}
