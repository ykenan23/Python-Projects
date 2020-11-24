import random
matriks1=[]
matriks2=[]
for i in range(0,8):
    matriks1.append([])
    matriks2.append([])
    for j in range(0,8):
        matriks1[i].append(random.randint(0,1))
        matriks2[i].append(random.randint(0, 1))

print("Rastgele Matriks1:" , matriks1)
print("Rastgele Matriks2:" , matriks2)

hamming_uzakligi=0
for i in range(0,8):
    for j in range(0,8):
        if matriks1[i][j] == matriks2[i][j]:
            continue
        else:
            hamming_uzakligi = hamming_uzakligi + 1
print(hamming_uzakligi)