# Algorithms Project 1 - RSA
# Objective: implement RSA Encryption and apply it to digital signature
import pandas as pd
import numpy as np
import sys
from random import randint
from math import gcd
import hashlib


# check if n is prime (most likely a prime)
def FermatPrimalityTest(n):
    # print(n)
    a = randint(2, n - 3)
    
    # fremat test with 2 iterations
    for i in range(a, a + 2):
        # make sure that n is not co-prime of a
        if gcd(i, n) != 1:
            return False

        # actual fermat test
        if (pow(i, n -1, n)) != 1:
            return False
    
    return True


def gcdExtended(a, b): 
    # Base Case 
    if a == 0 : 
        return b,0,1
    
    # recursive call
    gcd,x1,y1 = gcdExtended(b%a, a) 
     
    # Update x and y  
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y 


def RSA_key_generation():
    # Initialize primes p and q to small values for start
    p = 10
    q = 10
    
    # Generate a prime p
    while not FermatPrimalityTest(p):
        p = randint(pow(2, 511), pow(2, 512))
    
    # Generate a prime q
    while not FermatPrimalityTest(q):
        q = randint(pow(2, 511), pow(2, 512))   
    
    # Public key
    e = 65537

    # Calculate n and phi_n
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Calculate the modular multiplicative inverse of e (private key)
    gcd, d, i = gcdExtended(e, phi_n)
    
    # If d is negative, convert it to a positive value by adding phi n
    if d < 0:
        d = d + phi_n

    # Save the generated keys to CSV files
    pq = pd.Series([p, q])
    en = pd.Series([e, n])
    dn = pd.Series([d, n])
    pq.to_csv("p_q.csv")
    en.to_csv("e_n.csv")
    dn.to_csv("d_n.csv")
    
    print("Done with key generation!")


def Signing(doc, key):

    # generate the hash based on the file contents 
    with open(doc, "r") as file:
        lines = file.readlines()
        content_lines = lines  # All but the last line

    # Concatenate the lines to form the content
    content = ''.join(content_lines)

    # Generate the SHA-256 hash based on the content
    hash_object = hashlib.sha256(content.encode())
    h = hash_object.hexdigest()   
   
    # sign the hash, then cast the hash as a hex value
    n = int(pd.read_csv('p_q.csv').iloc[1, 0]) * int(pd.read_csv('p_q.csv').iloc[1, 1]) # n = p*q 
    signature = pow(int(h, 16), int(key), n)
    signature = hex(signature)

    # copy the contents of the file to the signed file, then add the signature to the signed file
    with open(doc, 'r') as file:
        with open('file.txt.signed', 'w') as signed_file:
            for line in file:
                signed_file.write(line)

            signed_file.write("\n")
            signed_file.write(str(signature))

    print("\nSigned ...")


def verification(doc, key):
    # get the signature
    # Read the file and separate the last line
    with open(doc, "r") as file:
        lines = file.readlines()
        content_lines = lines
        signature = lines[-1]       # The last line

    # Concatenate the lines except the last (signature) to form the content
    content = ''.join(content_lines)
    content = content.rsplit('\n', 1)
    content = content[0]

    # Generate the SHA-256 hash based on the content
    hash_object = hashlib.sha256(content.encode())
    h = hash_object.hexdigest()
   
    # sign the hash, then cast the hash as a hex value
    n = int(pd.read_csv('p_q.csv').iloc[1, 0]) * int(pd.read_csv('p_q.csv').iloc[1, 1]) # n = p*q 
    new_sign = int(pow(int(h, 16), int(key), n))
    new_sign = hex(new_sign)

    if signature == new_sign:
        print("\nAuthentic!")
    else:
        print("\nModified!")


# No need to change the main function.
def main():
    # part I, command-line arguments will be: python yourProgram.py 1
    if int(sys.argv[1]) == 1:
        RSA_key_generation()
    # part II, command-line will be for example: python yourProgram.py 2 s file.txt
    #                                       or   python yourProgram.py 2 v file.txt.signed
    else:
        (task, fileName) = sys.argv[2:]
        if "s" in task:  # do signing
            doc = fileName
            key = pd.read_csv('d_n.csv').iloc[1, 1]
            Signing(doc, key)
        else:
            # do verification
            doc = fileName
            key = pd.read_csv('e_n.csv').iloc[1, 1]
            verification(doc, key)

    print("done!")


if __name__ == '__main__':
    main()
