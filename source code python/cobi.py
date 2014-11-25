def hari():
    bulan=['Nul','Mar','Apr','Mei','Juni','Juli','Agus','Sept','Okt','Nov','Des','Jan','Feb']
    nama1=raw_input('Masukkan nama pertama Anda: ')
    nama2=raw_input('Masukkan nama kedua Anda: ')
    print ('Masukkan tanggal lahir Anda sebagai berikut:')
    tanggal=raw_input('Anda dilahirkan pada tanggal berapa? ')
    bulan=raw_input('Anda dilahirkan pada bulan apa?(Index=>Mar:1,...,Jan=11,Feb=12) ')
    tahun=raw_input('Anda dilahirkan pada tahun berapa?(Jika lahir pada hari ke ')
    print nama1,' ', nama2,' lahir pada hari ke- ',tanggal
    print '0 berarti Minggu, 1 berarti senin...6 means Sabtu'

hari()
