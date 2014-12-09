#include <stdio.h>

void printbits(char *data, unsigned bytes){
	printf("0b");
	unsigned i, b;
	for (i = 0; i < bytes; ++i)
		for (b = 0; b < 8; ++b)
			putchar((data[i] & (1 << b)) ? '1' : '0');
	putchar('\n');
}
