## README ##

I did this in 2016 and spent a lot of time trying to understand how to efficiently perform stuff like moduluses. This horrible mess is in `RSAencryption_experemental_files.py`. I have done a simple implementation of RSA in `RSAencryption.py`

This algorithm involves Alice generating the key that Alice and Bob are going to use. She then requests a public key from Bob, who will generate a private and a public key. Bob sends his public key to Alice who encrypts the key and sends the encrypted message to Bob who can decrypt the message using his public key.

Bob will generate the public and private keys by first chosing two large integers p and q. He will then compute n = p*q which will form one part of the public key. It is decomposing n into p and q which is the reason this key sharing scheme will be totally broken by quantum computers since one of the tasks quantum computers are good for is factorising numbers. 

Next the value of the Euler totient function is calculate as \Phi = (p-1) * (q-1). 

Now choose an integer between 1 and \Phi, this value must be coprime with \Phi and will be `e`. 

The private key d is found using 

(d * e) % \Phi = 1

Now calculate d where d = `e`<sup>-1</sup>

encrypted_m = message<sup>e</sup> % n

message = encrypted_m<sup>d</sup> % n

This can also be used to sign messages:

EXPLAIN RSA SIGNING HERE

### Sources ###

* https://en.wikipedia.org/wiki/RSA_(cryptosystem)