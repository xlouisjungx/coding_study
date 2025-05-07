#include <stdio.h>

int main(void) {
    int num[10000], N = 0, comN = 0;

    scanf("%d %d", &N, &comN);

    for(int i = 0; i < N; i++) {
        scanf("%d", &num[i]);
    }

    for(int i = 0; i < N; i++) {
        if(num[i] < comN) {
            printf("%d ", num[i]);
        }
    }
    printf("\n");
    return 0;
}