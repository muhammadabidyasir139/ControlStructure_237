nilai = int(input("Masukkan banyaknya angka: "))

def fibonacci(nilai):
   sequence = [0, 1]
   a, b = 0, 1
   while b < nilai:
    sequence.append(b)
    a,b = b, a + b 
   
   return sequence
result = fibonacci(nilai)
print (f"Hasilnya: {result}")