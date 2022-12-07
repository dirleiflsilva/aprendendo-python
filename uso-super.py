# super explicado
# https://realpython.com/python-super/
class Base:
    def __init__(self):
        print('Base.__init__')

class Filha1(Base):
    def __init__(self):
        #Base.__init__(self)
        super().__init__()
        print('Filha1.__init__')

#b = Base()
#print('-'*25)
#f1 = Filha1()

class Filha2(Base):
    def __init__(self):
        #Base.__init__(self)
        super().__init__()
        print('Filha2.__init__')

class Filha3(Filha1, Filha2):
    def __init__(self):
        #Filha1.__init__(self)
        #Filha2.__init__(self)
        super().__init__()
        print('Filha3.__init__')

f3 = Filha3()
print(Filha3.__mro__)
