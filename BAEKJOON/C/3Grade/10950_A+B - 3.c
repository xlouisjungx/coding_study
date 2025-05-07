#include <stdio.h>

int main(void) {
    int N = 0, num1 = 0, num2 = 0;

    scanf("%d", &N);

    for(int i = 0; i < N; i++) {
        scanf("%d %d", &num1, &num2);
        printf("%d\n", num1 + num2);
    }

    return 0;
}