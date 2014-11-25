class inputpendekerror(Exception):
    def __init__(self,panjang,minimal):
        Exception.__init__(self)
        self.panjang=panjang
        self.minimal=minimal
try:
    teks=raw_input('Ketikkan sesuatu')
    minimal_panjang=4
    if panjangminimal_panjang:
        raise inputpendekerror(panjang.minimal_panjang)
except EOFError:
    print '\n kenapa sudah EOF?'
except KeyboardInterrupt :
    print 'anda membatalkan operasi'
except inputpendekerror:
    print 'input terlalu pendek' 
else:
    print 'anda mengetikkan "%s" ' %teks
