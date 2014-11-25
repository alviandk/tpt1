def menu():
    print 'Menu Program'
    print '------------'
    print '1. Faktorisasi Bilangan'
    print '2. KPK dari Dua Bilangan'
    print '3. Ketemu'
    print '4. Program hari'
    print''


def faktor():
    u=input('Angka: ')
    x=1
    print '[',
    while x<=u:
        if u%x==0:
            print x,',',
        x=x+1
    
    print ']'

def kpk():
    a=input('masukkan a = ')
    b=input('masukkan b = ')
    atas=a*b
    sisa=a%b
    while sisa<>0:
        a=b
        b=sisa
        sisa=a%b
    fpb=b
    kpk=atas/fpb
    print 'KPK dari ',a,' dan ',b,' adalah ',kpk
    

def ketemu():
    a=input('masukkan tanggal a = ')
    b=input('masukkan tanggal b = ')
    atas=a*b
    sisa=a%b
    while sisa<>0:
        a=b
        b=sisa
        sisa=a%b
    fpb=b
    kpk=atas/fpb
    print 'Si a dan si B akan bertemu pada',kpk,' hari lagi'
    
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

lagi='y'
while (lagi != 'n'):
    menu()
    pilih=input('Masukkan pilihan [1-3]: ')

    if pilih == 1:
        faktor()
    elif pilih ==2:
        kpk()
    elif pilih == 3:
        ketemu()
    elif pilih == 4:
        hari()
    else:
        print 'Pilihan Anda Tidak Ada pada Program !!'
    lagi=raw_input('Mau Menjalankan program lagi [y/n]')
