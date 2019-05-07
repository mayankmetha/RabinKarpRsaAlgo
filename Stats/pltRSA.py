#!/usr/bin/python3

import matplotlib.pyplot as plt
import sys

fin = open(sys.argv[1],'r')
inpSize = []
etim = []
dtim = []
for _ in fin.readlines():
    x = _.split(",")
    inpSize.append(int(x[0]))
    etim.append(float(x[1]))
    dtim.append(float(x[2]))
fin.close()

plt.title("RSA Algorithm")
plt.plot(inpSize,etim,label='Encryption')
plt.plot(inpSize,dtim,label='Decrpytion')
plt.xlabel('Number of Inputs')
plt.ylabel('Time (in µs)')
#plt.xscale('log')
#plt.yscale('log')
plt.grid(True)
plt.legend()
plt.show()