nilai1 = input ("masukan angka pertama : ")
nilai2 = input ("masukan angka kedua : ")
nilai3 = input ("masukan angka ketiga : ")

if int(nilai1) > int(nilai2) and int(nilai1) > int(nilai3):
    print("Nilai terbesar adalah " + str(nilai1))
elif int(nilai2) > int(nilai1) and int(nilai2) > int(nilai3):
    print("Nilai terbesar adalah " + str(nilai2))
elif int(nilai3) > int(nilai1) and int(nilai3) > int(nilai2):
    print("Nilai terbesar adalah " + str(nilai3))