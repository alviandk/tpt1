def faktor():
    u=input('Angka: ')
    x=1
    print '[',
    while x<=u:
        if u%x==0:
            print x,',',
        x=x+1
    
    print ']'

faktor()
