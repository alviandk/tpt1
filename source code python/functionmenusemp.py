def menu():
    print 'Menu Program'
    print '------------'
    print '1. Pangkat Bilangan'
    print '2. Faktorial Bilangan'
    print '3. Deret Fibonacci'
    print''


def fibo(x):
    if x ==1:
        return 0
    if x ==2:
        return 1
    if x>2:
        return fibo(x-1)+fibo(x-2)

    for i in range(1,x):
        print 'suku ke ',i,' deret fibonacchi ini = ',fibo(i)
        print""

def pangkat(x,y):
    
    if y==0:
        return 1
    else:
        return x * pangkat(x,y-1)
        

def faktorial(x): 
    if x==1:
        return 1
    if x>1:
        return x*faktorial(x-1)


lagi='y'
while (lagi != 'n'):
    menu()
    pilih=input('Masukkan pilihan [1-3]: ')

    if pilih == 1:
        x=input('masukkan bilangan :')
        y=input('masukkan pangkat  :')
        print x,' pangkat ', y,' = ',pangkat(x,y)
    elif pilih ==2:
        x=input('masukkan bilangan : ')
        print x,' faktorial = ',faktorial(x)        
    elif pilih == 3:
        x=input('masukkan bilangan : ')
        for i in range(1,x):
            print 'suku ke ',i,' deret fibonacchi ini = ',fibo(i)
            print""

    else:
        print 'Pilihan Anda Tidak Ada pada Program !!'
    lagi=raw_input('Mau Menjalankan program lagi [y/n]')
