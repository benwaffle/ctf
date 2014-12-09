#include <stdio.h>
void printbits(char *data, unsigned bytes);
int main() {
	float *a = malloc(sizeof(float)*2);
	a[0] = 100000000000;
	a[1] = 100000000000;
	//scanf("%lf", a);
	printf("float = %f, next float = %f, double = %f\n", *a, *(a+1), *(double*)a);
	printf("     float = "); printbits(a, sizeof(float));
	printf("next float = "); printbits(&a[1], sizeof(float));
	printf("double     = "); printbits(a, sizeof(double));
}
