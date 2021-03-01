#NAMA : M Hilal Alhamdy
#KELAS : K01
#DESKRIPSI : TUCIL 2 STIMA(Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer))

from DerajatMasuk13519024 import *

def eliminasi(file):
    for i in file:
        for j in file:
            cek = True
            if (j != " " and j !="." and j !="" and j !="\n") :
                for k in listmatkul:
                    if (j == k):
                        cek = False
                if (cek == True):
                    listmatkul.append(j)

file = open("Test14.txt", "r")
print("Masukkan Nama File: daftarmatkul.txt")
baca = file.readlines()

listmatkul = [] #Array yang isinya daftar Mata Kuliah
for line in baca: #Menghilangkan semua tanda baca dari inputan yang akan di pindahkan ke Array listmatkul
    hapustanda = line.rstrip('\n').rstrip('.').replace(",","").split(' ')
    listmatkul.append(hapustanda)

#fungsi yang mencari derajat_masuk yang memiliki nilai 0
def derajatnol(X): 
    newarray = []
    for i in range(len(X)):
        if (len(X[i]) == 1):
            (newarray.append(i))
    return newarray

#fungsi yang mengurutkan DAG yang akan di jadikan keluaran per-semester
def topologicalSort(X):
    matakuliah = []
    while (len(X) > 0):
        newderajat = derajatnol(X)
        variabelsolusi = []

        for i in range(len(newderajat)):
            variabelsolusi.append(X[newderajat[i]])
            X.pop(newderajat[i])
            for j in range(len(X)):
                for k in range(len(X[j])):
                    if ((X[j][k]) == variabelsolusi[i]):
                        X[j].remove(variabelsolusi[i])

        matakuliah.append(variabelsolusi)
    return matakuliah
    
#array global penyimpanan list mata kuliah
matakuliah = []

#fungsi lain dari topologocal sort
def TopologicalSort(derajat):
    if (len(derajat) == 1):
        matakuliah.append([derajat[0][0]])
        return (derajat[0])
    else:
        TopologicalSort(DerajatMasuk(derajat, matakuliah))

#fungsi yang mengecek apakah keluaran tidak lebih dari 1 setiap semester
def cekprint(derajat, indeks):
    cek = False
    for i in range(indeks):
        for j in range(len(matakuliah[i])):
            if( matakuliah[i][j] == derajat):
                cek = True
            
    return cek

print("-")
#pemanggilan fungsi Topological sort dengan inputan dari file
TopologicalSort(listmatkul)

#arraylist yang menyimpan
semester = []

#proses pengeluaran output
for i in range (len(matakuliah)):
    semesterfix = []
    for j in range(len(matakuliah[i])):
        if ( not(cekprint(matakuliah[i][j], i))):
            semesterfix.append(matakuliah[i][j])
    if (len(semesterfix) != 0):
        semester.append(semesterfix)

for i in range (len(semester)):
    print("Semester ", i+1, " : ", end=" ")
    for j in range(len(semester[i])):
        print(semester[i][j], end=" ")
    print(" ")








