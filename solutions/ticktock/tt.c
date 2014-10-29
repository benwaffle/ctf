#include <stdio.h>
#include <stdbool.h>
#include <gmp.h>

const unsigned int mods[][2] = {{1, 2}, {2, 3}, {8, 13}, {4, 29}, {130, 191}, {343, 397}, {652, 691}, {858, 1009}, {689, 2039}, {1184, 4099}, {2027, 7001}, {5119, 10009}, {15165, 19997}, {15340, 30013},{29303, 70009}, {42873, 160009}, {158045, 200009}};

const int nummods = sizeof(mods)/sizeof(mods[0]);

mpz_t n, tmp, toadd;

inline int check() {
    for (int i = 0; i < nummods; i++)
        if (mpz_mod_ui(tmp, n, mods[i][1]) != mods[i][0])
            return i;
    return -1;
}

inline void lcmlower(int pos) {
    mpz_set_ui(toadd, mods[0][1]);
    for (int i = 1; i < pos; ++i)
        mpz_lcm_ui(toadd, toadd, mods[i][1]);
}

int main() {
    mpz_init_set_ui(n, 1);
    mpz_init(tmp);
    mpz_init(toadd);

    // part 1
    int fpos = -2;
    while (fpos != -1) {
        int curpos = check();
        if (curpos == -1) break;
        if (curpos != fpos) {
            fpos = curpos;
            lcmlower(fpos); 
        }
        mpz_add(n, n, toadd); 
    } 

    printf("part 1: "); mpz_out_str(stdout, 10, n); printf("\n");
/*
    // part 2
    mpz_t modulo; mpz_init_set_d(modulo, 200009*160009L);
    mpz_t num2; mpz_init_set_ui(num2, 2);

    while ((mpz_powm(tmp, n, num2, modulo), mpz_cmp_ui(tmp, 1)) != 0) {
        mpz_add_ui(num2, num2, 1);
    }

    printf("part 2: "); mpz_out_str(stdout, 10, num2); printf("\n");*/
}
