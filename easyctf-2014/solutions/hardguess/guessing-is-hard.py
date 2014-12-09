#THE MEANEST GUESSING GAME EVER
"""
since my server has no randomness I'll just have to us random instead of os.urandom which isn't even implemented, still, I'm sure random good enough
"""
import random 
flag="You_will_have_to_hax_the_real_version_to_get_this"
random_secret=random.random()
#now all you have to do is type in my secret, good luck
print random_secret
data = raw_input("What is your guess? ")
print random_secret),' = secret'
print bin(float(data)),' = input'

if float(data)==random_secret:
    print flag
else:
    print "NOPE",float(data),"!=",random_secret

