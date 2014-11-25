try:
    file=open('d:/BARANG.txt')
    print 'nama file',file.name
    print 'mode pembacaan file',file.mode
except IOError,e:
    print 'error bro karena',e
              
