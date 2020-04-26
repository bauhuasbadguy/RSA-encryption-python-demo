#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:22:57 2020

@author: stuart
"""

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


def privkey(n, pub, totient):
    #can be done either using pure random guessing (try every number to find a functional private key)
    #or by the backwards Euclidean Algorithm
    #here y is set to -2 in the equation (e*x)+(tot*y)=1 x is the private key and e is the public one
    key = modinv(pub, totient)
    return key


def findprimes(startnumber):
    trynumber = startnumber
    exitnumber = 1
    #make sure we only look at even numbers
    if startnumber % 2 == 0:
        trynumber -= 1

    while exitnumber != 0:
        trynumber += 2
        
        for i in range(3, int(((trynumber + 1) / 2) + 2), 2):
            
            remainder = trynumber % i
            if remainder == 0:
                
                break

        if remainder != 0:
            exitnumber = 0
    return trynumber



def genrandpub(tot):
    key = 0
    while key == 0:
        start = random.randint(int(tot/5),int((tot/5) *4))

        val = findprimes(start)

        if tot % val != 0 and val <= tot:
            key = val

    return key



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

#now find a publc key, e. This must 
pub = 17

#the message, the value of this must be less than n
message = 1042

#now find the private key, d. This must 
priv = 413

#Alice will now encrypt Bob's message with her private key.
#encrypted = message^(e) % n
encrypted = pow(message, priv, n)

#Bob decrypts Alices signed message, if it matches the message he sent he has confirmed Alice's identity.
#message = encrypted^(d) % n
decrypted = pow(encrypted, pub, n)

print('Uncrypted')
print(message)
print('encrypted')
print(encrypted)
print('decrypted')
print(decrypted)

