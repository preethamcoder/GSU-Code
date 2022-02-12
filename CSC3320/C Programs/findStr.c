#include <stdio.h> 
#include <string.h> 
int main(){ 
    char input[22]; 
    char shortest[22]; 
    char longest[22]; 
    printf("Enter a word: "); 
    scanf("%s", input); 
    strcpy(shortest, input); 
    strcpy(longest, input); 
    while(strlen(input) != 4){ 
        if(strcmp(input, longest) > 0){ 
            strcpy(longest, input); 
        }else if(strcmp(input, shortest) < 0){ 
            strcpy(shortest, input); 
        } 
        printf("Enter a word: "); 
        scanf("%s", input); 
    } 
    printf("Shortest word is: %s\n", shortest); 
    printf("Longest word is: %s\n", longest); 
    return 0; 
} 
