## README ##

I did this in 2016 and spent a lot of time trying to understand how to efficiently perform stuff like moduluses. This horrible mess is in `RSAencryption_experemental_files.py`. I have done a simple implementation of RSA in `RSAencryption.py` as well as an example of RSA signing in `RSASigning.py`.

This algorithm involves Alice generating the key that Alice and Bob are going to use. She then requests a public key from Bob, who will generate a private and a public key. Bob sends his public key to Alice who encrypts the key and sends the encrypted message to Bob who can decrypt the message using his public key.

Bob will generate the public and private keys by first chosing two large integers p and q. He will then compute n = p*q which will form one part of the public key. It is decomposing n into p and q which is the reason this key sharing scheme will be totally broken by quantum computers since one of the tasks quantum computers are good for is factorising numbers. 

Next the value of the Euler totient function is calculated as &Phi; = (p-1) * (q-1). 

Now choose an integer between 1 and &Phi;, this value must be coprime with &Phi; and will be e, which will form part of the public key (n, e). 

The private key, d, is the multiplicative inverse of e(mod &Phi;). In other words d is the value where (d * e)%&Phi;=1

encrypted_m = message<sup>e</sup> % n

message = encrypted_m<sup>d</sup> % n

In this way Alice and Bob exchange a secret key which they can then use to encrypt a further message exchange using a faster encryption system like blowfish or AES.

This tool also be used to sign a file as coming from a specific person.

If Bob wants Alice to sign a file he will send a message which he asks Alice to encrypt using e, which is now the private key, not the public key. Now Alice sends Bob the encrypted message along with d and n which are the public keys here. By decrypting the message Bob has confirmed that Alice is the owner of her private key. Allowing her to sign any other files she wants to send to Bob by asking Bob to send another message to encrypt thereby ensuring all subsequent files originate from the same source.

### IMPORTANT NOTE ###

I am some guy in a room. You should never use the code here for real encryption purposes. I hope it will help you understand the principal of RSA encryption but this has not been checked by anyone with any real expertise or training in cryptography.

### Sources ###

* https://en.wikipedia.org/wiki/RSA_(cryptosystem)
* 