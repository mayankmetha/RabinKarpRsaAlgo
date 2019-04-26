#!/usr/bin/python3

import sys
import os
import random
import math
import time
from termcolor import colored

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

# RSA 
def rsa(inFile,outFile):
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
    str1 = "("+str(e)+","+str(n)+")"
    str2 = "("+str(d)+","+str(n)+")"
    print(colored("Key 1 = ",'yellow',attrs=['bold']),colored(str1,'white',attrs=['bold']))
    print(colored("Key 2 = ",'yellow',attrs=['bold']),colored(str2,'white',attrs=['bold']))
    f = open(outFile+"Keys","w")
    f.write(str(e)+","+str(n)+"\n"+str(d)+","+str(n))
    f.close()
    fin = open(inFile,"r")
    foute = open(outFile+"Encrypted","w")
    foutd = open(outFile+"Decrypted","w")
    lines = 0
    etime = 0
    dtime = 0
    for _ in fin.readlines():
        lines += 1
        num = str(_.strip())
        arr = []
        arr2 = []
        start = 0
        stop = 0
        start = time.time()
        for x in num:
            arr.append(str(pow(int(x),d,n)))
        stop = time.time()
        etime += (stop-start)
        foute.write((",".join(arr))+"\n")
        start = time.time()
        for x in arr:
            arr2.append(str(pow(int(x),e,n)))
        stop = time.time()
        dtime += (stop-start)
        foutd.write(("".join(arr2))+"\n")
    foute.close()
    foutd.close()
    fin.close()
    i = 0
    a1 = []
    a2 = []
    f = open(inFile,"r")
    for _ in f.readlines():
        a1.append(_.strip())
    f.close()
    f = open(outFile+"Decrypted","r")
    for _ in f.readlines():
        a2.append(_.strip())
    f.close()
    for _ in range(0,lines):
        if a1[_] == a2[_]:
            i += 1
    str3 = "Deciphered Correctly = "
    str4 = "%d of %d"%(i,lines)
    print(colored(str3,'yellow',attrs=['bold']),colored(str4,'white',attrs=['bold']))
    str5 = "Encryption Time = "
    str6 = str(etime*pow(10,6))+" µs"
    str7 = "Decrpytion Time = "
    str8 = str(dtime*pow(10,6))+" µs"
    print(colored(str5,'green',attrs=['bold']),colored(str6,'white',attrs=['bold']))
    print(colored(str7,'green',attrs=['bold']),colored(str8,'white',attrs=['bold']))

def main():
    inFile = None
    outFile = None
    if len(sys.argv) == 5:
        if sys.argv[1] == '-i':
            inFile = sys.argv[2]
        elif sys.argv[3] == '-i':
            inFile = sys.argv[4]
        else:
            print(colored("Usage Error: ./rsa.py -i <input file> -o <output file base name>",'magenta',attrs=['bold']))
            exit(1)
        if sys.argv[1] == '-o':
            outFile = sys.argv[2]
        elif sys.argv[3] == '-o':
            outFile = sys.argv[4]
        else:
            print(colored("Usage Error: ./rsa.py -i <input file> -o <output file base name>",'magenta',attrs=['bold']))
            exit(1)
    else:
        print(colored("Usage Error: ./rsa.py -i <input file> -o <output file base name>",'magenta',attrs=['bold']))
        exit(1)
    print(colored("Input File = ",'red',attrs=['bold']),colored(inFile,'white',attrs=['bold']))
    print(colored("Keys File = ",'red',attrs=['bold']),colored(outFile+"Keys",'white',attrs=['bold']))
    print(colored("Encryption File = ",'red',attrs=['bold']),colored(outFile+"Encrypted",'white',attrs=['bold']))
    print(colored("Decryption File = ",'red',attrs=['bold']),colored(outFile+"Decrypted",'white',attrs=['bold']))
    rsa(inFile,outFile)

main()