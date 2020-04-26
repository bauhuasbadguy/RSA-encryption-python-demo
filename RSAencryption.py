#encryption functions

import random


#I tried many times to make this myself and ended up copying a version off stack exchange because mine
#always broke
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('There is no multiplicative inverse of', a, 'and', m)
    return x % m



###################################
### End of function definitions ###
###################################

#This is the starting point. Alice will generate two prime numbers, p and q.
#Here I am using 61 and 53 since they are in the wikipeida example. Normally you
#would expect these to be much much larger
p = 61
q = 53

#now calculate n. This will form part of the public key and will be used in both
#encryption and decryption
n = p * q

print('n =', n)

#now calculate the totient function. This will be used to generate the private key
tot = (p - 1) * (q - 1)

#now find a public key, e. This must be coprime to the totient function and is chosen by Alice who has
#generated a series of values coprime to the totient function.
pub = 17

#now find the private key, d. This must be the modular multiplicative inverse of 1%tot. i.e.
#(d * e) % tot = 1
#d = e^-1 (mod tot)
#calculate this value using the backwards Euclidean Algorithm. The function is given here but you
#don't need to fully understand it to get the basic idea of RSA encryption
priv = modinv(pub, tot)

#the message, provided by Alice. This will be the key Alice and Bob use for further communication.
#The value of this must be less than n for RSA to work properly
message = 1042


#verifiy this is the multiplicative inverse here by showing (e*d)%totient = 1
verification = (pub * priv) % tot
print('verify private key is the multiplictive inverse:', verification)

#Bob encrypts his message using the public key
#encrypted = message^(e) % n
encrypted = pow(message, pub, n)

#Alice will decrypt Bobs message and now they have a shared key they can use to encrypt messages between
#one another
#message = encrypted^(d) % n
decrypted = pow(encrypted, priv, n)

print('Uncrypted')
print(message)
print('encrypted')
print(encrypted)
print('decrypted')
print(decrypted)






