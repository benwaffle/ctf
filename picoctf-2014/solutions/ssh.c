#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>

static int frobcmp(const char *str) {
	int rc = 0;
	size_t len = strlen(str);
	char *s = strdup(str);
	memfrob(s, len);

    printf("%s\n", s);

	free(s);
	return rc;
}

int main() {
	frobcmp("CGCDSE_XGKIBCDOY^OKFCDMSE_XLFKMY");
}
