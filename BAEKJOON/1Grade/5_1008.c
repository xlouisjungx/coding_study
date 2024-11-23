#include <stdio.h>

int main(void) {
    int num1, num2;
    scanf("%d %d", &num1, &num2);
    printf("%f", (num1*0.1) / (num2*0.1));
    return 0;
}