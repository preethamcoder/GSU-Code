#include <stdio.h>
fun(int a);
int main(){
	int a = 10;
	printf("Return value of function is an integer: %d", fun(10));
	return 0;
}
fun(int a){
	return(a*a);
}
