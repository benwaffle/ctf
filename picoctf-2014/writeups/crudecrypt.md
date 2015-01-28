Crude Crypt
====
Without proper maintainers, development of Truecrypt has stopped! CrudeCrypt has emerged as a notable alternative in the open source community. The author has promised it is 'secure' but we know better than that. Take a look at the [code](https://picoctf.com/problem-static/binary/CrudeCrypt/crude_crypt.c) and read the contents of `flag.txt` from the server! The problem is at /home/crudecrypt/crude_crypt on the shell server. 

Solution
----
The code is a simple program to encrypt & decrypt files. The user input, in this case, is the file that will be encrypted or decrypted. The function `check_hostname` is called when decrypting a file and uses `strncpy` and `strlen` on the host field of `struct file_header`, so we will use this for a buffer overflow. To craft our malicious encrypted file, we will use the same functions and libraries as crude_crypt to encrypt a `char[]`. We must start our file with the `magic_number` in the code. We use an arbitrary file size (the code that uses it will not be reached). Now, the program expects a hostname up to 32 chars long, but it uses strlen when reading it. Here we put our shellcode and return address, followed by `0x00`. The file is 60 bytes, and the host is 48, which covers `char saved_host[HOST_LEN]` and `file_header* header`. Then we just encrypt this buffer and write it to a file. Now, this malicious input can be used on crude_crypt to get a shell.
There are a few modifications that need to be made to the shellcode to make it work, in this case. Using gdb on our shell code, we can see that certain registers get overwritten. We can fix `%edx` using `mov %esp,%edx`, and fix `%esp` with `mov $0xffffd62b,%esp`. We compile these into object files and use objdump to find the opcodes, and then replace some of the nops with these instructions. This allows us to successfully get a shell.

Flag
----
`writing_software_is_hard`
