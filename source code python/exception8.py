try:
    x=input('masukkan bilangan pertama:')
    y=input('masukkan bilangan kedua:')
    z=x/y
    print

except (ZeroDivisionError,TypeError,NameError),e:
    print 'error bro karena',e
    
