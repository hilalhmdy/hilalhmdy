#NAMA : M Hilal Alhamdy
#KELAS : K01
#DESKRIPSI : TUCIL 2 STIMA(Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer))

#fungsi yang menghitung derajat_masuk, dan akan di urutkan sesuai topological sort
def DerajatMasuk(derajat, matakuliah): 

    #arraylist yang menyimpan nilai derajatmasuk dari setiap simpul
    derajatmasuk =[]
    for i in derajat:
        derajatmasuk.append(len(i)-1)

    #arraylist yang menyimpan nilai busur yang telah di hapus di simpul
    doblecase =[]

    for i in range(len(derajatmasuk)):
        if (derajatmasuk[i] == 0):
            doblecase.append(derajat[i][0])
        else:
            continue
    
    for i in range(len(derajatmasuk)):
        if (derajatmasuk[i] == 0):
            caseawal = derajat[i][0]
            break
        else:
            continue

    derajat.remove([caseawal])
    matakuliah.append(doblecase)

    #array yang yang menyimpan nilai akhir dari proses penghapusan DAG
    newderajat = []
    for i in range (len(derajat)):
        if (caseawal in derajat[i]):
            (derajat[i]).remove(caseawal)
            newderajat.append(derajat[i])
        else:
            newderajat.append(derajat[i])
    return (newderajat)
