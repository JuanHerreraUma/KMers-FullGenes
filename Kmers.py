x = open('HSapiens_chr1.fa')
a = x.read()
x.close()
b = a[113:]
c = b.replace("N", "")
lectura = c

print("Longitud de la secuencia:", len(lectura))


def cmers(lectura, k):
    kFreq = {}

    for i in range(0, len(lectura) - k + 1):

        kmer = lectura[i:i + k]

        if kmer in kFreq:
            kFreq[kmer] += (1 / len(lectura))

        else:
            kFreq[kmer] = 1 / (len(lectura))

    return kFreq


n = int(input("Determine el número de n mers: "))

rf = cmers(lectura, n)

ListRF = [[sequence, rf[sequence]] for sequence in rf]

ListRF.sort(reverse=True)

print(ListRF)
