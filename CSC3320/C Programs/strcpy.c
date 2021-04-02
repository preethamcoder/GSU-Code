#include <stdio.h>
char *strCpy(char *strDest, const char *strSrc);
int main(){
	char src[] = "System Level Programming"; 
	char dest[100]; 
	printf("Original String: %s\n", src); 
	printf("Destination String: %s", strCpy(&dest, &src)); 
	return 0;
}
char* strCpy(char* strDest, const char* strSrc){ 
    int i = 0; 
    while(strSrc[i] != '\0'){ 
        strDest[i] = strSrc[i]; 
        i++; 
    } 
    strDest[i] = '\0'; 
    return strDest; 
} 
