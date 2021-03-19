#include <stdio.h>
int main(){
int letters, words, space;
char character;
printf("Enter a sentence: \n");
while((character=getchar()) != '\n'){
	if(character != ' '){
		if(!space){
			words++;
			space=1;
		}
	letters++;
	}else{
		space = 0;
}
}
	printf("Average word length : %.1f", (double)(letters/words));
	return 0;
}
