#include <stdio.h> 
int main(){ 
    int item; 
    double price; 
    int quantity; 
    char date[10];
    printf("Enter item number:"); 
    scanf("%d", &item); 
    printf("Enter unit price:"); 
    scanf("%lf", &price); 
    printf("Enter quantity:"); 
    scanf("%d", &quantity); 
    printf("Enter purchase date:");
    scanf("%s", date); 
    double total = price * quantity; 
    printf("Item\tUnit Price\tQTY\tPurchase Date\tTotal Amount\n"); 
    printf("%d\t$%9.2lf\t%d\t%s\t$%9.2lf\n\n", item, price, quantity, date, total); 
    return 0; 
}
