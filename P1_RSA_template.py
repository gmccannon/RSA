# Algorithms Project 1 - RSA
# Objective: implement RSA Encryption and apply it to digital signature
import pandas as pd
import numpy as np
import sys
from random import randint


# check if p is prime (most likely a prime)
def FermatPrimalityTest(n):
    print(n)
    a = randint(2, n - 2)
    
    # fremat test with 2 iterations
    for i in range(a, a + 2):
        # make sure that n is not co-prime of a
        if gcd(i, n) != 1:
            return False

        # actual fermat test
        if (pow(i, n -1, n)) != 1:
            return False
    
    return True


def RSA_key_generation():
    p = randint(pow(2, 511), pow(2, 512))
    q = randint(pow(2, 511), pow(2, 512))

    pq = pd.Series([p,q])
    # en = pd.Series([e,n])
    # dn = pd.Series([d,n])
    pq.to_csv("p_q.csv")
    # en.to_csv("e_n.csv")
    # dn.to_csv("d_n.csv")
    print("done with key generation!")


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
