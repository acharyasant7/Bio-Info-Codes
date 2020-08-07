import numpy as np
import matplotlib.pyplot as plt

seq = ''
with open(r"GCF_000091665.1_ASM9166v1_genomic.fna") as file:
    for line in file:
        if line[0] != '>':
            seq = seq + line.strip()

string = list(seq)
arrayskew = np.zeros(len(string))
arraypos = np.zeros(len(string))
skew = 0
for i in range(0, len(string), 1):
    if string[i] == "G":
        skew = skew +1
    elif string[i] == "C":
        skew = skew -1
    arrayskew[i] = skew
    arraypos[i]= i

fig = plt.figure()
plt.plot(arraypos, arrayskew)
plt.xlabel("Position of Nucleotide")
plt.ylabel("Skew")
plt.title("Skew with Position of Nucleotide")

    
    