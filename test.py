import sys
from random import randint
from math import gcd


def FermatPrimalityTest(n):
    print(n)
    a = randint(2, n - 2)
    
    for i in range(a, a + 2):
        # make sure that n is not co-prime of a
        if gcd(i, n) != 1:
            return False

        # fermat test
        if (pow(i, n -1, n)) != 1:
            return False
    
    return True


print(FermatPrimalityTest(int(sys.argv[1])))

