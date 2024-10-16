nilai = int(input("Masukan angka : "))
def odd(nilai):
    sequence = []
    for i in range (1, nilai):
        if i % 2 != 0:
            sequence.append(i)

    return sequence
hasil = odd(nilai)
print (f"hasilnya adalah : {hasil}")

    