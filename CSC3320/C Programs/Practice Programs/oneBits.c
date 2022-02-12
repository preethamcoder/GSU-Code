#include <stdio.h>
int bitsret(int *n);
int main(){
	int num = 10;
	printf("The number of 1 bits in %d \n", num);
	printf("is %d\n", bitsret(&num));	
	return 0;
}
int bitsret(int *n){
	int count = 0;
	while(*n > 0){
		*n &= (*n-1);
		count += 1;
	}	
	return count;
}
