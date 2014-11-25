
try:
    teks=raw_input('berikan sesuatu :')
except EOFError:
    print '\n kenapa sudah EOF?'
except KeyboardInterrupt :
    print 'anda membatalkan operasi'
else:
    print 'anda mengetikkan "%s" ' %teks
