import time
try:
    f=open('d:/coba.txt')
    while True:
        baris=f.readline()
        if len(baris)==0:
            break
        print baris
        time.sleep(2)
except KeyboardInterrupt:
    print '%s anda membatalkan operasi'
finally:
    f.close()
    print '\n file ditutup'
