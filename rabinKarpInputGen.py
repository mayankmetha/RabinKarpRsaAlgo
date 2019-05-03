#/usr/bin/python3

import os
import sys
import random
import string

def main(size):
    fin = open('rbIn','w')
    fin.write(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits,k=size)))
    fin.close()

main(int(sys.argv[1]))