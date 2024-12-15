#include <stdio.h>

int main(void) {
    int hour = 0, minute = 0, time = 0, plus = 0;

    scanf("%d %d", &hour, &minute);
    scanf("%d", &time);

    minute = minute + time;
    plus = minute / 60;

    if(plus != 0) {
        if(hour + plus >= 24) {
            printf("%d %d\n", ((hour + plus) - 24), (minute - (60 * plus)));    
        }
        else {
            printf("%d %d\n", hour + plus, minute - (60 * plus));
        }
    }
    else {
        printf("%d %d\n", hour, minute + plus);
    }
    return 0;
}