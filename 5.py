import random
class auto:    
    def bip(self):
        print("bip")
    def __init__(self,mass,v,hp,price):
        self.mass=mass
        self.v=v
        self.hp=hp
        self.price=price
    @property
    def mass(self):
        return self.__mass
    @mass.setter
    def mass(self, m):
        if(m>=0):
            self.__mass=m
        else:
            raise ValueError
    @property
    def v(self):
        return self.__v
    @v.setter
    def v(self, _v):
        if(_v>=0):
            self.__v=_v
        else:
            raise ValueError
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, h):
        if(h>=0):
            self.__hp=h
        else:
            raise ValueError
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, p):
        if(p>=0):
            self.__price=p
        else:
            raise ValueError

class bigauto(auto):
    def __init__(self,mass,v,hp,price,pricep):
        super().__init__(mass,v,hp,price)
        self.pricep=pricep        
    @property
    def pricep(self):
        return self.__pricep
    @pricep.setter
    def pricep(self, pr):
        if(pr==0 or pr==1):
            self.__pricep=pr
        else:
            raise ValueError
    def bip(self):
        print("bip bip")
    def out(self):
        print("bigauto razgruzhen")

class Myiter:    
    def __init__(self):
        self.count=3
        self.num=1
    def __next__(self):
        self.num=self.num*self.count
        return self.num

def mygen(val):
    while(val>0):
        val-=1
    yield val

auto1=auto(2000,3.5,300,3500000)
auto1.bip()
print(auto1.mass,auto1.v,auto1.hp,auto1.price, sep="|") 
auto2=bigauto(4000,6.5,500,400000,1)
auto2.bip()
auto2.out()
i=0
it=Myiter()
while(i<10):
    next(it)
    i=i+1
print(next(it))
m,n=7,7
matr=[[random.randrange(0,2) for y in range(m)]for x in range(n)]
for i in range(n):
    print(matr[i])

        
for i in range(m):
    for j in range(n):
        if(matr[i][j]==1 and i>0 and j>0):
            matr[i][j]=min(matr[i-1][j-1],matr[i][j-1],matr[i-1][j])+1

maxi=0
for i in range(n):
    maxi=max(max(matr[i]),maxi)
print(maxi)
