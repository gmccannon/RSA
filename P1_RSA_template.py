# Algorithms Project 1 - RSA
# Objective: implement RSA Encryption and apply it to digital signature
import pandas as pd
import numpy as np
import sys
from random import randint
from math import gcd


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


def test(mess, e, d, n):
    cypher = pow(mess, e, n)
    print(cypher)

    decMess = pow(cypher, d, n)
    print(decMess)


def gcdExtended(a, b): 
    # Base Case 
    if a == 0 : 
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a) 
     
    # Update x and y  
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y 


def RSA_key_generation():
    p = 10
    q = 10
    # generate a prime p
    while not FermatPrimalityTest(p):
        p = randint(pow(2, 511), pow(2, 512))
    # generate a prime q
    while not FermatPrimalityTest(q):
        q = randint(pow(2, 511), pow(2, 512))   
    # write p and q
    
    # public key
    e = 65537
    n = p*q
    phi_n = (p - 1)*(q - 1)

    gcd, d, i = gcdExtended(e, phi_n)
    if d < 0:
        d = d + phi_n

    print(f"d = {d}")
    print(f"n = {p*q}")
    print( f"e*d = {(e*d) % ((p-1)*(q-1))}" )

    pq = pd.Series([p,q])
    en = pd.Series([e,n])
    dn = pd.Series([d,n])
    pq.to_csv("p_q.csv")
    en.to_csv("e_n.csv")
    dn.to_csv("d_n.csv")
    print("done with key generation!")

    test(901050306030300306020, e, d, n)


def Signing(doc, key):
    match = False
    # to be completed
    print("\nSigned ...")


def verification(doc, key):

    match = False
    # to be completed
    if match:
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
            doc = None  # you figure out
            key = None  # you figure out
            Signing(doc, key)
        else:
            # do verification
            doc = None   # you figure out
            key = None   # you figure out
            verification(doc, key)

    print("done!")


if __name__ == '__main__':
    main()
