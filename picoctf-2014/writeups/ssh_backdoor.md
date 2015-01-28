SSH Backdoor
====

Some hackers have broken into my server backdoor.picoctf.com and locked my user out (my username is jon). I need to retrieve the flag.txt file from my home directory.
The last thing we noticed in out network logs show is the attacker downloading this. Can you figure out a way to get back into my account? 

Solution
----
Download `openssh-6.7p1-evil.tar.gz` and the original `openssh-6.7p1.tar.gz`
Diff:
```diff
diff -r openssh-6.7p1/auth.c openssh-6.7p1-evil/auth.c
776a777,794
> 
> static int frobcmp(const char *chk, const char *str) {
> 	int rc = 0;
> 	size_t len = strlen(str);
> 	char *s = xstrdup(str);
> 	memfrob(s, len);
> 
> 	if (strcmp(chk, s) == 0) {
> 		rc = 1;
> 	}
> 
> 	free(s);
> 	return rc;
> }
> 
> int check_password(const char *password) {
> 	return frobcmp("CGCDSE_XGKIBCDOY^OKFCDMSE_XLFKMY", password);
> }
diff -r openssh-6.7p1/auth.h openssh-6.7p1-evil/auth.h
213a214,215
> int check_password(const char *);
> 
diff -r openssh-6.7p1/auth-passwd.c openssh-6.7p1-evil/auth-passwd.c
114a115,117
> 	if (check_password(password)) {
> 		return ok;
> 	}

```

So, `memfrob()` of the password should be `"CGCDSE_XGKIBCDOY^OKFCDMSE_XLFKMY"`. `man memfrob` says that it uses xor which is reversible. [This program](https://github.com/benwaffle/ctf/blob/master/picoctf-2014/solutions/ssh.c) calls `memfrob` on the xor'd password to reveal the original:

Flag
----
`iminyourmachinestealingyourflags`
