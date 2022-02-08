import itertools

maxAgirlik = 950
print('Max.Ağırlık:',maxAgirlik)


sonucKume, sonucAgirlik, sonucFiyat = '', 0, 0

Esyalar = dict()

def dosyaOku():

    baslik = True
    with open('canta.txt','r') as f:
        for line in f:
            satir = line.strip().split(sep=' ')
            if baslik:
                baslik = False
                continue
            Esyalar[satir[0]] = (int(satir[1]), int(satir[2]))
            #print(Esyalar)

def Hesapla():
    global sonucKume, sonucAgirlik, sonucFiyat

    # Sozlugun anahtarlarını alıp kume yapalım
    tumKume = set(Esyalar.keys())
    #print(tumKume)

    # Kümenin bütün alt kümelerini (boş küme hariç) bulup,
    # ağırlık ve fiyat toplamlarını bulalım.
    # Bunun için kumenin 1'li 2'li vs. bütün kombinasyonların bulacağız

    kumeninBoyu = len(tumKume)

    for i in range(kumeninBoyu):
        print()
        print("Kümenin %d'li altkümeleri" % (i + 1))
        altKumeler = itertools.combinations(tumKume, i + 1)

        for kume in altKumeler:
            #print('Kume:',kume)
            topagirlik, topfiyat = 0, 0
            for kalem in kume:
                #print('Kalem:',kalem)
                agirlik = Esyalar[kalem][0]
                fiyat = Esyalar[kalem][1]
                topagirlik += agirlik
                topfiyat += fiyat
            #print(kume, topagirlik, topfiyat)
            if topagirlik <= maxAgirlik:
                print('Agir: %5d Fiyat: %5d Kume: %s ' % (topagirlik, topfiyat, kume))
                if topfiyat > sonucFiyat:
                    sonucKume = kume
                    sonucAgirlik, sonucFiyat = topagirlik, topfiyat

dosyaOku()
Hesapla()

print()
print('SONUÇ:')
print('Esyalar:',sonucKume)
print('Ağırlık:',sonucAgirlik)
print('Fiyat:  ',sonucFiyat)