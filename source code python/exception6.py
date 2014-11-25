listx=[1,2,3,4,5]
tuplex=[1,2,3,4,5]
dictionmay={'nama' : 'Abi','email' : 'ai@gmail.com'}

try:
    print listx[10]
except IndexError,e:
    print 'proses gagal karena:',e

try:
    print dictionmay['web']
except KeyError,e:
    print 'gagal karena:',e
    
