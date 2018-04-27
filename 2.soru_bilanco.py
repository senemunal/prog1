def donenHesapla(kh,ach,bh,ash,tmh):
    global donenVarlik
    donenVarlik=kh+ach+bh+ash+tmh
    return donenVarlik

def duranHesapla(bih,th,dh):
    global duranVarlik
    duranVarlik=bih+th+dh
    return duranVarlik

def kvykHesapla(bkh,sh):
    global kvyk
    kvyk=bkh+sh
    return kvyk

def uvykHesapla(bkh,bsh):
    global uvyk
    uvyk=bkh+bsh
    return uvyk

def aktiftoplam(donenVarlik,duranVarlik):
    global aktiftoplam
    aktiftoplam=donenVarlik+duranVarlik
    print("Aktif Toplamınız:",aktiftoplam)

def pasiftoplam(kvyk,uvyk,ozk):
    global pasiftoplam
    pasiftoplam=kvyk+uvyk+ozk
    print("Pasif Toplamınız:",pasiftoplam)

def farkAL(aktiftoplam,ptoplam):
    fark=ptoplam-aktiftoplam
    if(fark==0):
        print("Kapanış bilançosu doğru hesaplanmıştır",fark)
    else:
        print("Bilanço yanlış hesaplanmıştır")

kh=int(input("Kasa hesabınızı yazınız:"))
ach=int(input("Alınan çekler hesabınızı yazınız:"))
bh=int(input("Bankalar hesabınızı yazınız:"))
ash=int(input("Alınan senetler hesabınızı yazınız:"))
tmh=int(input("Ticari mallar hesabınızı yazınız:"))
bih=int(input("Binalar hesabınızı yazınız:"))
th=int(input("Taşıtlar hesabınızı yazınız:"))
dh=int(input("Demirbaş hesabınızı yazınız:"))
bkh=int(input("Banka kredileri hesabınızı yazınız:"))
sh=int(input("Satıcılar hesabınızı yazınız:"))
bkh=int(input("Banka kredileri hesabınızı yazınız:"))
bsh=int(input("Borç senetleri hesabınızı yazınız:"))
sh=int(input("Sermaye hesabınızı yazınız:"))
ozk=int(input("Öz sermayeyi yazınız:"))


donenHesapla(kh,ach,bh,ash,tmh)
duranHesapla(bih,th,dh)
kvykHesapla(bkh,sh)
uvykHesapla(bkh,bsh)
aktiftoplam(donenVarlik,duranVarlik)
pasiftoplam(kvyk,uvyk,ozk)
farkAL(aktiftoplam,pasiftoplam)

#modülün çağırılması
import modul2

modul2.donenHesapla(kh,ach,bh,ash,tmh)
modul2.duranHesapla(bih,th,dh)
modul2.kvykHesapla(bkh,sh)
modul2.uvykHesapla(bkh,bsh)
modul2.aktiftoplam(donenVarlik,duranVarlik)
modul2.pasiftoplam(kvyk,uvyk,ozk)
modul2.farkAL(aktiftoplam,pasiftoplam)