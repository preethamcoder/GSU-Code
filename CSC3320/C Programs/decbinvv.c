#include <stdio.h>
#include <math.h>
int main(){
	int a[10], n;
	int i = 0;
	long long bin;
	int dec = 0, j = 0, rem;
	char c;
	printf("What do you want to convert to? (b/d)\t");
	scanf("%s", &c);
	if(c == 'b'){
		printf("Enter the decimal number: ");
		scanf("%d", &n);
		for(i=0;n>0;i++){    
			a[i]=n%2;    
			n=n/2;    
		}    
		printf("\nBinary of Given Number is=");    
		for(i=i-1;i>=0;i--){    
			printf("%d",a[i]);    
		}

	}else{
		printf("Enter the binary number: ");
		scanf("%lld", &bin);
		while(bin != 0){
			rem = bin % 10;
			bin /= 10;
			dec += rem * pow(2, j);
			j += 1;
		}		
		printf("\nNumber in decimal is %d\n", dec);
		}
		return 0;
}
