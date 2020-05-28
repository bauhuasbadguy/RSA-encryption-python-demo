## README ##

I did this in 2016 and spent a lot of time trying to understand how to efficiently perform stuff like moduluses. This horrible mess is in `RSAencryption_experemental_files.py`. I have done a simple implementation of RSA in `RSAencryption.py` as well as an example of RSA signing in `RSASigning.py`.

### RSA message sharing algorithm ###

This algorithm involves Alice having a message which she wants to send to Bob. Alice requests a public key from Bob, who will generate a private and a public key. Bob sends his public key to Alice who encrypts the message using the public key and sends the encrypted message to Bob who can decrypt the message using his private key.

Bob will generate the public and private keys by first choosing two large, prime integers p and q. He will then compute n = p*q which will form one part of the public key. The difficulty of breaking this encryption scheme is the difficulty of the task of decomposing n into p and q. However this is asl the reason this key sharing scheme will be totally broken by quantum computers since one of the tasks quantum computers are good for is factorising numbers. 

Next the value of the Euler totient function is calculated as &Phi; = (p-1) * (q-1). 

Now Bob chooses an integer between 1 and &Phi;, this value must be coprime with &Phi; and will be from now on known as e, which will form part of the public key (n, e). 

The private key, d, is the multiplicative inverse of e(mod &Phi;). In other words d is the value where (d * e)%&Phi;=1. In order to encrypt the message Alice will now perform the calculation:

encrypted_m = message<sup>e</sup> % n

And Bob will recover the secret message using the calculation:

message = encrypted_m<sup>d</sup> % n

In this way Alice and Bob exchange a message over an insecure channel without risking interception. Potentially the secret message may be a second secret key which they can then use to encrypt a further messages using a faster encryption system like blowfish or AES.

### Digital signatures ###

This tool also be used to sign a file as coming from a specific person.

If Bob wants Alice to sign a file he will send a message, which can be publicly read, and he asks Alice to encrypt it using e, which is now the private key, not the public key. Now Alice sends Bob the encrypted message along with d and n which are the public keys here. By decrypting the message Bob has confirmed that Alice is the owner of her private key. Allowing her to sign any other files she wants to send to Bob by asking Bob to send another message to encrypt thereby ensuring all subsequent messages originate from the same source.

### IMPORTANT NOTE ###

I am some guy in a room. You should never use the code here for real encryption purposes. I hope it will help you understand the principals of RSA encryption but this has not been checked by anyone with any real expertise or training in cryptography.

### Sources ###

* https://en.wikipedia.org/wiki/RSA_(cryptosystem)