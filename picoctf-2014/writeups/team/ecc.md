David: ECC -100

The actual procedure required to solve this problem is quite simple once you gain a fair background in the relevant content. Elliptic Curve Cryptography, as its name implies, exploits the characteristics of points on an elliptic curve. You are given the equation of the elliptic curve. While the value of b is missing, it can be easily identified since the point on the curve C is given. 

The decryption method is M = d * C mod n. You can use some computation using softwares, and Sage has some good libraries for elliptic curves. After defining an elliptic curve, M can be identified by multiplying point C by d. Finally, simply plug those two values into the Python script and the flag will be printed. 

`ELLIPTIC CURVES ARE FUN`

