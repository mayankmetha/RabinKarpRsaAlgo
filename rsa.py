#!/usr/bin/python3

import sys
import os
import random
import math

# GCD
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

# Extended GCD
def extgcd(a,b):
    if b == 0:
        return (a,1,0)
    else:
        (d1,x1,y1) = extgcd(b,a%b)
    d,x,y = d1,y1,(x1-(a//b)*y1)
    return (d,x,y)

# Multiplicative Modulo Inverse
def mulInv(a,n):
    d,x,y = extgcd(a,n)
    if d == 1:
        return int(x%n)

# Eulers totient for Prime numbers
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

# Generates prime numbers
def genPrime():
    x = 1
    while not isPrime(x):
        x = random.getrandbits(31)
    return x

# Primality check
# True if prime
def isPrime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    limit = int(math.sqrt(n))+1
    for i in range(3,limit,2):
        if n%i == 0:
            return False
    return True

# Relative prime check
# True if relative prime
def isRelPrime(a,b):
    if gcd(a,b) == 1:
        return True
    else:
        return False

# Main 
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
    foute = open("rsaEnc","w")
    foutd = open("rsaDec","w")
    lines = 0
    for _ in fin.readlines():
        lines += 1
        num = str(_.strip())
        arr = []
        arr2 = []
        for x in num:
            arr.append(str(pow(int(x),d,n)))
        foute.write((",".join(arr))+"\n")
        for x in arr:
            arr2.append(str(pow(int(x),e,n)))
        foutd.write(("".join(arr2))+"\n")
    foute.close()
    foutd.close()
    fin.close()
    i = 0
    a1 = []
    a2 = []
    f = open("rsaIn","r")
    for _ in f.readlines():
        a1.append(_.strip())
    f.close()
    f = open("rsaDec","r")
    for _ in f.readlines():
        a2.append(_.strip())
    f.close()
    for _ in range(0,lines):
        if a1[_] == a2[_]:
            i += 1
    print("Deciphered Correctly:%d out of %d"%(i,lines))
main()