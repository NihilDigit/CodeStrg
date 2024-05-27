#include<stdio.h>
void print(int i);

int main(void) {
    for (int i = 0; i < 10000; i++) {
        printf("%d %d ", i, i/2);
        print(i);
    }
    return 0;
}

void print(int i) {
    printf("%d ", i/3);
}