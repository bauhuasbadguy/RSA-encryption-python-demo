#encryption functions
import math
import random
import time
import multiprocessing as mp
import string
from multiprocessing import Pool
#need to make the finding of the public key way more efficient don't construct a list of potentials
#just pick one

#output = mp.Queue()

#########################
#wild last ditch attempts
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

###########################


#functions for the preporation of data
def stringtonumbers(mesage):
    output = []
    mesage = mesage.lower()
    for i in mesage:
        x = ord(i)
        output.append(x)

    return output

def numberstowords(numbers):
    output = ''
    
    for i in numbers:
        x = chr(i)
        output = output + chr(i)
    return output


def findprimes(startnumber):
    trynumber = startnumber
    exitnumber = 1
    #make sure we only look at even numbers
    if startnumber % 2 == 0:
        trynumber -= 1

        
    while exitnumber != 0:
        trynumber += 2
        
        for i in range(3, ((trynumber + 1) / 2) + 2, 2):
            
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
            
        
    
        
def potentpublist(totient):
    #list of potential values for the public key
    candlist = []

    for i in range(1, totient):
        candlist.append(findprimes(i))
    candlist = list(set(candlist))
    
    for val in candlist:
        
        if totient % val == 0 or val >= totient:
            
            candlist.remove(val)
            
    
    return candlist

def privkey(n, pub, totient):
    #can be done either using pure random guessing (try every number to find a functional private key)
    #or by the backwards Euclidean Algorithm
    #here y is set to -2 in the equation (e*x)+(tot*y)=1 x is the private key and e is the public one
    key = modinv(pub, totient)
    return key

def priveytrialanderror(n, pub, tot):
    
    incidence = 0
    key = 0
    found = False
    while found == False:
        key += 1
        result = (key * pub) % tot
        if result == 1:
            incidence += 1
            if incidence == 1:
                found = True
    return key



def generatekeys(minp, minq):

    p = findprimes(minp)
    q = findprimes(minq)
    n = long(p)*long(q)

    totient = long(p-1) * long(q-1)
    #print 'totient is ' + repr(totient)
    for k in range(totient, 1, -1):
        k = findprimes(k)
        if k < totient:
            remainder = totient % k
            if remainder != 0:
                
                break
    
    
    return [long(p),long(q),n,totient,long(k)]

def encryptnumber(m, k, n):
    c1 = long(1)
    m = long(m)
    for i in range(k):
        c1 = c1 * m
    cf = c1 % n
    return cf

def decryptnumber(c, pr, n):

    c = long(c)
    m1 = long(1)
    count = 0
    for i in range(pr):
        m1 = m1 * c
        count = count + 1
    mf = m1 % n

    return mf




##############################################
#Start time saving versions of the algorithms#
##############################################


def findchinesecoeffsdecrpt(q, p, n, priv):

    d = priv
    #wikipedia method
    dp = (d) % (p - 1)
    dq = (d) % (q - 1)
    qinv = modinv(q, p)
    #print '****'
    #print dp
    #print dq
    #print qinv
    #print '******'
    return [dp, dq, qinv]




def decryptwtchina(A, p, q, dp, dq, qinv):

    m1 = long(1)

    for i in range(dp):
        m1 = m1 * A

    M1 = m1 % p

    m2 = long(1)
    
    for i in range(dq):
        m2 = m2 * A


    M2 = m2 % q


    if M1 < M2:

        #h = (qinv * ((M1 + ((q/p)*p))-M2)) % p
        h = (qinv * (M1 - M2)) % p

    else:
        h = (qinv * (M1 - M2)) % p



    s = M2 + (h*q)
    #print s
    return s
    


def findchinesecoeffsdecrpt(q, p, n, pub):

    e = pub
    #wikipedia method
    ep = (e) % (p - 1)
    eq = (e) % (q - 1)
    qinv = modinv(q, p)
    #print '****'
    #print dp
    #print dq
    #print qinv
    #print '******'
    return [ep, eq, qinv]

def encryptwtchina(mesage, p, q, ep, eq, qinv):

    A = mesage

    dp = ep
    dq = eq
    
    m1 = long(1)

    for i in range(dp):
        m1 = m1 * A

    M1 = m1 % p

    m2 = long(1)
    
    for i in range(dq):
        m2 = m2 * A


    M2 = m2 % q


    if M1 < M2:

        #h = (qinv * ((M1 + ((q/p)*p))-M2)) % p
        h = (qinv * (M1 - M2)) % p

    else:
        h = (qinv * (M1 - M2)) % p


    s = M2 + (h*q)
    #print s
    return s

################
#Binary methods#
################

#L modular exponential
#Find B=(A^E)%n
#def Lmodexp(A, E, n):
    

######################
#Start implementation#
######################

    
#n and k are public keys p and q are used to find the keys and are secret
t = time.time()
p = findprimes(346)
q = findprimes(284)


n = p * q
tot = (p - 1) * (q - 1)
print('Found n,it\'s '+ repr(n))
pqntottime = time.time() - t
pub = genrandpub(tot)

pubkeytime = time.time() - pqntottime - t
mesage = 10473


#pub = candlist[rand.randint(int(length(candlist)/10), length(candlist))]
print('Found public key it\'s ' + repr(pub))
priv = privkey(n, pub, tot)
#priv = priveytrialanderror(n, pub, tot)
privkeytime = time.time() - pubkeytime - t
print('Found private key, it\'s ' + repr(priv))
#p = 137
#q = 131
#n = 17947
#pub = 3
#priv = 11787

print(mesage)
encrypted = encryptnumber(mesage, pub, n)
A = encrypted
encryptiontime = time.time() - privkeytime - t
print(encrypted)
decrypted = decryptnumber(encrypted, priv, n)
decryptiontime = time.time() - encryptiontime - t
print(decrypted)

print('Generating p,q,n and totient function took ' + repr(pqntottime) + 's')
print('--------------------------------------------------')
print('Generating the public key took ' + repr(pubkeytime) + 's')
print('--------------------------------------------------')
print('Generating the private key took ' + repr(privkeytime) + 's')
print('--------------------------------------------------')
print('Encrypting the data took ' + repr(encryptiontime) + 's')
print('--------------------------------------------------')
print('Dycrypting the data took ' + repr(decryptiontime) + 's')




printtime = time.time() - decryptiontime - t

chinaexponenttime = time.time() - printtime - t
[dp, dq, qinv] = findchinesecoeffsdecrpt(q, p, n, priv)

result = decryptwtchina(A, p, q, dp, dq, qinv)

chinatime = time.time() - chinaexponenttime - t

print(result)

print('*******')
print('The chinese remainder system decryption took ' + repr(chinatime))




[ep, eq, qinv] = findchinesecoeffsdecrpt(q, p, n, pub)


chinaencryptexponenttime = time.time() - chinatime - t



result1 = encryptwtchina(mesage, p, q, ep, eq, qinv)

chinaencrypttime = time.time() - chinaencryptexponenttime - t
print('**********')
print(result1)
print(chinaencrypttime)

