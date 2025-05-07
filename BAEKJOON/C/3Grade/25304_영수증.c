#include <stdio.h>

int main(void) {
    int total = 0, money = 0, many = 0, N = 0, sum = 0;

    scanf("%d", &total);
    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        scanf("%d %d", &money, &many);
        sum += money * many;
    }

    if(sum == total) printf("Yes\n");
    else printf("No\n");

    return 0;
}