#encryption functions

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




#This is the starting point. Alice will generate two prime numbers, p and q
p = 61
q = 53

#now calculate n. This will form part of the public key and will be used in both
#encryption and decryption
n = p * q

print('n =', n)

#now calculate the totient function. This will be used to generate the private key
tot = (p - 1) * (q - 1)

#now find a publc key, e. This must be coprime to the toient function and is chosen by Alice from a list
#of candidates
pub = 17

#the message, provided by Alice. This will be the key Alice and Bob use for further communtication.
#The value of this must be less than n for RSA to work properly
message = 1042

#now find the private key, d. This must be the modular multiplicative inverse of 1%tot. i.e.
#(d * e) % tot = 1
priv = 413

#Bob encrypt his message using the public key
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






