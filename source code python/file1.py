try:
    file=open('d:/coba.txt','w')
    file.mode
    file.write('1. Alvian Dwi K, Sistem Informasi Gunadarma \n')
    file.write('2. Anindita Ayu P, Sistem Informasi Gunadarma \n')
    file.write('3. Citra Dewi L, Sistem Informasi Gunadarma \n')
    file.close()
    file.closed
except IOError,e:
    print 'error bro karena',e
