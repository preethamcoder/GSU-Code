#include<stdio.h> 
void split_time(long total_sec, int *hr, int *min, int  *sec);
int main(){ 
	int n, hr, min, sec; 
	printf("Enter seconds: "); 
	scanf("%d",&n); 
	split_time(n, &hr, &min, &sec);
	printf("Converted format: %d hour %d mins %d secs", hr, min, sec); 
	return 0; 
} 
void split_time(long total_sec, int *hr, int *min, int *sec){ /* Write the statements to calculate hr, min and sec  */ 
	*sec = 0;
	*min = 0;
	*hr = 0;
	*sec = total_sec % 60;
	total_sec = total_sec / 60;
	*min = total_sec % 60;
	total_sec = total_sec / 60;
	*hr = total_sec % 60;
	total_sec = total_sec / 60;
}
