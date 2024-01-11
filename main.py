usia = int(input('Berapa usia Anda? '))

# OPERATOR
# == sama dengan
# != tidak sama dengan
# < kurang dari sama dengan
# <= kurang dari sama dengan
# > lebih dari
# >= lebih dari sama dengan

if usia == 0:
    print('belum lahir')
elif usia > 0 and usia <= 5:
    print('balita')
elif usia > 5 and usia <= 10:
    print('anak - anak')
elif usia > 10 and usia <= 18:
    print('remaja')
elif usia > 18 and usia <= 25:
    print('dewasa')
else:
    print('.... pengecualian ....')
