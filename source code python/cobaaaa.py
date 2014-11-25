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
kpk()
