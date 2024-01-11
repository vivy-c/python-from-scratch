# gabungan input dengan operasi aritmatika
a = input('masukan angka pertama = ') # ouput inputan string misal 3 menjadi '3'
b = input('masukan angka kedua = ') # inputan 8 menjadi '8'
# c = a + b # hasilnya menjadi 38

# harus di konvert dulu menjadi integer
c = int(a) + int(b) # disini hasilnya menjadi 12
d = int(a) - int(b)
e = int(a) * int(b)
f = int(a) / int(b)
# f = int(a) // int(b) # pakai dua garis kalau ingin dibulatkan kebawah hasilnya

hello = 'hello nama saya ' + 'hello test'

print('hasilnya penjumlahannya adalah ' + str(c) + ' pengurangannya ' + str(d) + ' pembagiannya ' + str(e) + ' perkaliannya ' + str(f)) #disini jadi string
print(hello)
