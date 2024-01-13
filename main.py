saldo_awal = 5000
deposit = input('Input desposit : ')

saldo_total = saldo_awal + int(deposit)
hutang = 50_000

if saldo_total >= hutang :
    sisa_saldo = saldo_total - hutang
    print('Sisa uang : ' + str(sisa_saldo))
else:
    print('saldo kurang')

