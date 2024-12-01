#include <stdio.h>

int main(void) {
    int num1 = 0, num2 = 0, num3 = 0, num4 = 0, num5 = 0, num6 = 0;

    scanf("%d", &num1);
    scanf("%d", &num2);

    num3 = ((num2 - (num2 - (num2 % 100))) % 10) * num1;
    printf("%d\n", num3);

    num4 = ((num2 - (num2 - (num2 % 100))) / 10) * num1;
    printf("%d\n", num4);

    num5 = (num2 - (num2 % 100)) / 100 * num1;
    printf("%d\n", num5);

    num6 = num3 + (num4 * 10) + (num5 * 100);

    printf("%d\n", num6);
    return 0;
}