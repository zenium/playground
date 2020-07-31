#include <stdio.h>

void main(void)
{
    int N;
    int x = 0;
    double sum = 0.0;
    puts("\n Summing 1.0/x for x between 1 and N.\n");
    printf(" Please enter an integer N greater than 1: ");
    scanf("%i", &N);
    if (N<=1) {
        printf("\n Input value %i is too small.\n\n", N);
    }
    else {
        while (x<N) {
            ++x;
            sum+=1.0/x;
        }
    }
    printf(" The sum is %g \n\n", sum);
}