#!/usr/bin/python3

import matplotlib.pyplot as plt
import sys

fin = open(sys.argv[1],'r')
inpSize = []
tim = []
for _ in fin.readlines():
    x = _.split(",")
    inpSize.append(int(x[0]))
    tim.append(float(x[1]))
fin.close()

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.title("Rabin-Karp String Matching")
plt.plot(inpSize,tim)
plt.xlabel('Input Pattern Size (linear scale)')
plt.ylabel('Time (in ms)')
plt.grid(True)
plt.subplot(2, 1, 2)
plt.plot(inpSize,tim)
plt.xlabel('Input Pattern Size (log scale)')
plt.ylabel('Time (in ms)')
plt.grid(True)
plt.xscale('log')
plt.show()