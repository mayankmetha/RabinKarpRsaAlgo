#!/usr/bin/python3

import sys
import os
import random
import math

#gcd
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

#extended gcd
def extgcd(a,b):
    if b == 0:
        return (a,1,0)
    else:
        (d1,x1,y1) = extgcd(b,a%b)
    d,x,y = d1,y1,(x1-(a//b)*y1)
    return (d,x,y)

#multiplicative Inverse
def mulInv(a,n):
    d,x,y = extgcd(a,n)
    if d == 1:
        return int(x%n)

#eulers totient for Prime numbers
def phi(n):
    result = n
    p = 2
    while (p**2) <= n:
        if (n%p) == 0:
            while (n%p) == 0:
                n = n//p
            result = result*(1.0-(1.0/p))
        p += 1
    if n > 1:
        result = result*(1.0-(1.0/n))
    return int(result)

# generates prime numbers
def genPrime():
    x = 1
    while not isPrimeBrute(x):
        x = random.getrandbits(32)
    return x

# Naive primality check
# True if prime
def isPrimeBrute(n):
    if n <= 1:
        return False
    for a in range(2,n-1):
        if n%a == 0:
            return False
    return True

# Relative prime check
# True if relative prime
def isRelPrime(a,b):
    if gcd(a,b) == 1:
        return True
    else:
        return False
    
def main():
    p = genPrime()
    q = genPrime()
    n = p*q
    phiN = phi(p)*phi(q)
    e = 0
    for i in range(2,phiN):
        e = i
        if isRelPrime(e,phiN):
            break
    d = mulInv(e,phiN)
    print("Key1=(%d,%d)"%(e,n))
    print("Key2=(%d,%d)"%(d,n))
    f = open("rsaKeys","w")
    f.write(str(e)+","+str(d)+","+str(n))
    f.close()
    fin = open("rsaIn","r")
    fout = open("rsaEnc","w")
    for _ in fin.readlines():
        tmp = pow(int(_),e,n)
        fout.write(str(tmp)+"\n")
        print("Encrypting %d as %d"%(int(_.strip()),tmp))
        tmp2 = pow(tmp,d,n)
        print("Decrypting %d as %d"%(tmp,tmp2))
        i = 0
        if int(_.strip()) == tmp2:
            i += 1
    print(i)
    fout.close()
    fin.close()

main()