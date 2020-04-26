#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#RSA signing

import random

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
        raise ValueError
    return x % m


###################################
### End of function definitions ###
###################################


#In this example Bob needs to verify Alice's identiy so he sends Alice a message
#to encrypt. She encrypts the message using d, which was the public key when we were
#sharing keys but is now the private key. She then sends the encrypted message to Bob along
#with the public key. By decrypting the message to recover the original message Bob has verified Alice's
#identity.


#This is the starting point. Alice will generate two prime numbers, p and q
p = 61
q = 53

#now calculate n. This will form part of the public key and will be used in both
#encryption and decryption
n = p * q

print('n =', n)

#now calculate the totient function. This will be used to generate the private key
tot = (p - 1) * (q - 1)

#now find a private key, e. This must be coprime to the totient function and is chosen by Alice.
#She must keep this to sign further messages.
e = 17

#now find the public key, d. This must be the modular multiplicative inverse of 1%tot
#i.e. (D * e) % tot = 1
d = modinv(e, tot)

#the message to be used to generate the signature, sent by Bob. The value of this must be less than n.
message = 1042

#Alice will now encrypt Bob's message with her private key.
#encrypted = message^(e) % n
encrypted = pow(message, d, n)

#Bob decrypts Alice's signed message, if it matches the message he sent he has confirmed Alice's identity.
#message = encrypted^(d) % n
decrypted = pow(encrypted, e, n)

print('Uncrypted')
print(message)
print('encrypted')
print(encrypted)
print('decrypted')
print(decrypted)

