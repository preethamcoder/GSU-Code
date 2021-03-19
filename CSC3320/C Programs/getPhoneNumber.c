#include <stdio.h>
int main() {
    char phoneInput[13];
    char phoneRes[12];
    int i = 1;
    printf("Enter Phone Number - [(999)999-9999]:\n");
    scanf("%s", phoneInput);
    for (i = 1; i < 13; i++) {
        if (i == 4) {
            phoneRes[i - 1] = '-';
        }
        else {
            phoneRes[i - 1] = phoneInput[i];
        }
    }
    printf("You entered %s\n", phoneRes);
    return 0;
}
