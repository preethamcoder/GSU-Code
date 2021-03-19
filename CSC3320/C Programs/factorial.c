#include <stdio.h>
int main(){
	int i = 1;
	long long k = 1;
	int j;
	printf("Enter the value of the number to compute the factorial:\n");
	scanf("%d", &j);
	if(j == 0){
		printf("The factorial of %d is 1.\n",j);
	}else if(j < 0){
		printf("The factorial of %d cannot be computed, as it is a negative number!", j);		
	}else{
		for(i = 1; i<(j+1); i++){
			k *= i;
		}
		printf("The factorial of %d is %lld.\n",j ,k);
	}
	return 0;
} 	
