#!/usr/bin/python3

# RSA Algo
# select 2 32=bit prime p and q
# n = p*q
# phi(n)
# relPrime(e,phi(n)) 1 < e < phi(n)
# d = mulInv(e,phi(n))
# key1 = (e,n)
# key2 = (d,n)
# cipher  = (m**e)mod(n)
# ptext = (m**d)mod(n)

import sys
import os
import random
import math
import sympy

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
        b = 1
        tmp = x*(b/d)
        return int(tmp%n)
    else:
        return 0

#eulers totient
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
    while not isPrime(x):
        print(x)
        x = random.getrandbits(32)
    return x

# AKS primality check 
# Complexity: Õ((log n)**12)
# True if prime
def isPrime(n):
    # step1: if n = a**b for integers a > 1 and b > 1, output composite.
    for b in range(2,math.ceil(math.log2(n))):
        a = n**(1/b)
        #print(a,b)
        if a.is_integer():
            print("Composite")
            return False
    # step2: Find the smallest r such that multiplicative order of n modulo r > (log2(n))**2.
    maxk = math.floor((math.log2(n)**2))
    maxr = max(3,math.ceil((math.log2(n)**5)))
    nextR = True
    r = 2
    while nextR and r < maxr:
        nextR = False
        k = 1
        while not nextR and k <= maxk:
            t1 = (n**k)%r
            nextR = (t1 == 1 or t1 == 0)
            k += 1
        r += 1
    r -= 1
    #print(r)
    #step3: If 1 < gcd(a,n) < n for some a ≤ r, output composite.
    a = r
    while a > 1:
        g = gcd(a,n)
        if g > 1 and g < n:
            return False
        a -= 1
        #print(a,n,g)
    #step4: If n ≤ r, output prime.
    if n <= r:
        return True
    #step5: polynomial modulo congruence based check
    limit = math.floor(math.sqrt(phi(r))*math.log2(n))
    for a in range(1,(limit+1)):
        x = sympy.poly("x")
        equ = sympy.trunc(sympy.rem((x + a)**n -(x**n + a), x**r - 1), n)
        #print(a,equ)
        if equ != 0:
            return False
    #step6: output prime otherwise
    return True

# Relative prime check
# True if relative prime
def isRelPrime(a,b):
    if gcd(a,b) == 1:
        return True
    else:
        return False

