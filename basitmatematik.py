#Basit matematik kütüphanesi

def ucebolunme(sayi):
    if sayi %3==0:
        print("3'e bölünür")
    else:
        print("3'e bölünmez")

def kendindenoncekisayi(sayi):
    sayi -= 1
    print(sayi)

def usalma(sayi,usalma1):
    sayi = sayi**usalma1
    print(sayi)

def karealanhesaplama(kenar):
    alan = kenar**2
    print(alan)

def dairenincevresinihesaplama(yaricap):
    print("Pi üç alınır.")
    yaricap = 2*yaricap*3
    print(yaricap)
