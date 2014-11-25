class manusia:
    asal='indonesia'
    def asalx(self,negara):
        self.asal=negara

class mahasiswa:
    umurx=20
    kompetensix=' '
    namax=' '

    def __init__(self,umur):
        self.umurx=umur

    def setnama(self,nama):
        self.namax=nama

class mahasiswaSI(manusia,mahasiswa):
    def __init__(self,kompetensi='SI TPT python'):
        self.kompetensix=kompetensi

    def tampilkanidentitas(self):
        print self.umurx
        print self.namax
        print self.asal
        print self.kompetensix
                  
    
