#include <stdio.h>

int main(void) {
    int hour = 0, minute = 0;

    scanf("%d %d", &hour, &minute);

    if(hour == 0) {
        if(minute < 45) {
            printf("%d %d\n", hour + 23, minute + 15);
        }
        else {
            printf("%d %d\n", hour , minute - 45);
        }
    }
    else  {
        if(minute < 45) {
            printf("%d %d\n", hour - 1, minute + 15);
        }
        else {
            printf("%d %d\n", hour , minute - 45);
        }
    }
    return 0;
}