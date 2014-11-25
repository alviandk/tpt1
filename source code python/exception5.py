x=30
try:
    print x/0
except:
    print 'proses perhitungan gagal'
print 'proses cetak ini masih dapat jalan'

try:
    print x/0
except ZeroDivisionError,e:
    print 'proses perhitungan gagal karena :',e
print 'proses cetak ini masih bisa jalan'
