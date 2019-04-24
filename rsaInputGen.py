#!/usr/bin/python3
import os
import sys
import random

def main(size):
    fin = open('rsaIn','w')
    for _ in range(size):
        i = random.randint(10**18,((10**19)-1))
        fin.write(str(i)+"\n")
    fin.close()

main(int(sys.argv[1]))