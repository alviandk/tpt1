class oop:
    def __init__(self):
        print 'contructor class oop'

class oop1(oop):
    def __init__(self):
        print 'constructor class oop1'
        oop.__init__(self)

anak=oop1()
