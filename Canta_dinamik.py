import itertools

maxAgirlik = 950
print('Max.Ağırlık:',maxAgirlik)

Canta = dict()

sonucAgirlik, sonucFiyat =  0, 0

Esyalar = dict()

def dosyaOku():
    baslik = True
    with open('canta.txt','r') as f:
        for line in f:
            satir = line.strip().split(sep=' ')
            if baslik:
                baslik = False
                continue
            Esyalar[satir[0]] = (int(satir[1]), int(satir[2]), float(int(satir[2])/int(satir[1])))
            # print('Eşya,Ağırlık,Fiyat,GramFiyatı')
            # print(Esyalar)

def EnDegerliyiAl(Esyalar, MaxKilo):
    global sonucAgirlik, sonucFiyat
    maxgramfiyat = -1
    maxkalem=''
    for kalem,(kilo,fiyat,gramfiyat) in Esyalar.items():
        if gramfiyat > maxgramfiyat and kilo <= MaxKilo:
            maxgramfiyat = gramfiyat
            maxkalem = kalem

    if maxgramfiyat > 0:
        Canta[maxkalem] = Esyalar[maxkalem]
        kalanAgirlik = MaxKilo - Canta[maxkalem][0]
        del Esyalar[maxkalem]
        sonucAgirlik += Canta[maxkalem][0]
        sonucFiyat += Canta[maxkalem][1]
        EnDegerliyiAl(Esyalar, kalanAgirlik)
    else:
        return

dosyaOku()
print(Esyalar)
EnDegerliyiAl(Esyalar, maxAgirlik)

print()
print('SONUÇ:')
print('Canta:', Canta)
print('Kalan Esyalar:',Esyalar)
print('Ağırlık:',sonucAgirlik)
print('Fiyat:  ',sonucFiyat)