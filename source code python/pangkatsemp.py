def pangkat(x,y):
    if y==0:
        return 1
    else
    return x * pangkat(x,y-1)
        
        
x=input('masukkan bilangan :')
y=input('masukkan pangkat  :')
print x,' pangkat ', y,' = ',pangkat(x,y)
