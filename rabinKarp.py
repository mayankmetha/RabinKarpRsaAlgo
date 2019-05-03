#!/usr/bin/python3

import sys
import os
import time
import re
from termcolor import colored

def getInput():
    x = input()
    regex = re.compile('[^A-Za-z0-9]')
    x = regex.sub('',x)
    return x

# 0-9 -> 0-9
# a-z -> 10-35
# A-Z -> 36-61
def mapping(x):
    if x>='A' and x<='Z':
        return int(ord(x)-ord('A')+36)
    elif x>='a' and x<='z':
        return int(ord(x)-ord('a')+10)
    else:
        return int(x)

def rbAlgo(T,P,d,q):
    validShifts = []
    n = len(T)
    m = len(P)
    d = 62
    h = pow(d,m-1,q)
    p = 0
    t = 0
    for i in range(0,m):
        p = (d*p + mapping(P[i]))%q
        t = (d*t + mapping(T[i]))%q
    for s in range(0,n-m+1):
        if p == t:
            flag = 0
            for _ in range(0,m):
                if P[_] != T[_+s]:
                    flag = 1
            if flag == 0:
                validShifts.append(str(s))
        if s < n-m:
            t = ((d*(t-(mapping(T[s])*h)))+(mapping(T[s+m])))%q
    return validShifts

def main():
    inFile = None
    outFile = None
    if len(sys.argv) == 5:
        if sys.argv[1] == '-t':
            inFile = sys.argv[2]
        elif sys.argv[3] == '-t':
            inFile = sys.argv[4]
        else:
            print(colored("Usage Error: ./rabinKarp.py -t <input file> -o <output file base name>",'magenta',attrs=['bold']))
            exit(1)
        if sys.argv[1] == '-o':
            outFile = sys.argv[2]
        elif sys.argv[3] == '-o':
            outFile = sys.argv[4]
        else:
            print(colored("Usage Error: ./rabinKarp.py -t <input file> -o <output file base name>",'magenta',attrs=['bold']))
            exit(1)
    else:
        print(colored("Usage Error: ./rabinKarp.py -t <input file> -o <output file base name>",'magenta',attrs=['bold']))
        exit(1)
    print(colored("Key in pattern:",'yellow',attrs=['bold']))
    patt = getInput()
    print(colored("Input File = ",'red',attrs=['bold']),colored(inFile,'white',attrs=['bold']))
    print(colored("Output File = ",'red',attrs=['bold']),colored(outFile,'white',attrs=['bold']))
    fin = open(inFile,'r')
    inp = ""
    for _ in fin.readlines():
        inp = inp+""+_
    fin.close()
    start = time.time()
    outp = rbAlgo(inp,patt,62,pow(2,32)-1)
    stop = time.time()
    fout = open(outFile,'w')
    fout.write("Algo : ")
    fout.write(",".join(outp))
    fout.write("\nFunc : ")
    matc = [str(m.start()) for m in re.finditer('(?=%s)'%(patt), inp)]
    fout.write(",".join(matc))
    fout.close()
    str1 = "Time = "
    str2 = str((stop-start)*pow(10,3))+" ms"
    print(colored(str1,'green',attrs=['bold']),colored(str2,'white',attrs=['bold']))

main()