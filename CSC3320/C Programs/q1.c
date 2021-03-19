#include <stdio.h>

int foo(int num)
{
	int rev_num = 0;
	while (num > 0)
	{
		rev_num = rev_num*10 + num%10;
		num /= 10;
	}
	return rev_num;
}
/*Driver program to test foo*/
int main()
	{
	int num = 1125;
	printf("Result is %d", foo(num));
	return 0;
}
