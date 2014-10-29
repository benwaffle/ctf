pub=0xc20a1d8b3903e1864d14a4d1f32ce57e4665fc5683960d2f7c0f30d5d247f5fa264fa66b49e801943ab68be3d9a4b393ae22963888bf145f07101616e62e0db2b04644524516c966d8923acf12af049a1d9d6fe3e786763613ee9b8f541291dcf8f0ac9dccc5d47565ef332d466bc80dc5763f1b1139f14d3c0bae072725815f
cdate=100
while gcd(pub,cdate) == 1:
    cdate = int(subprocess.check_output(["sh", "-c", "nc vuln2014.picoctf.com 51818 | tail -1"]).strip('\n'), 16)

# do some more math, get p and q, punch in RSA calculator (http://www.mobilefish.com/services/rsa_key_generation/rsa_key_generation.php), punch the pub/priv keys in another with message (http://www.nmichaels.org/rsa.py), and you've got the flag
