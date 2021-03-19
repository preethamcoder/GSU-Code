#include <stdio.h>
int main(void){
	unsigned int inp;
	int fin;
	printf("Enter the number\n");
	scanf("%d", &inp);
	fin = (inp << 3) + ~inp;
	printf("value is %d\n", fin);
	return 0;
}
