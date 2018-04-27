def eoHesapla(x, y, z, m, n):
    eo = ((x + y + z) / m / n) * 100
    print("YBS-1 GRUBUNUN ETKİLEŞİM ORANI=", eo)
    if (eo > 0.20):
        print("YBS-1 GRUBUNUN ETKİLEŞİM ORANI BAŞARILIII!!")
    else:
        print("YBS-1 GRUBUNUN ETKİLEŞİM ORANI BAŞARISIZ!!")


def eo2Hesapla(k, a, b, c, d):
    eo2 = ((k + a + b) / c / d) * 100
    print("YBS-2 GRUBUNUN ETKİLEŞİM ORANI=", eo2)
    if (eo2 > 0.20):
        print("YBS-2 GRUBUNUN ETKİLEŞİM ORANI BAŞARILIII!!")
    else:
        print("YBS-2 GRUBUNUN ETKİLEŞİM ORANI BAŞARISIZ!!")


def eo3Hesapla(e, f, g, h, l):
    eo3 = ((e + f + g) / h / l) * 100
    print("YBS-3 GRUBUNUN ETKİLEŞİM ORANI =", eo3)
    if (eo3 > 0.20):
        print("YBS-3 GRUBUNUN ETKİLEŞİM ORANI BAŞARILIII!!")
    else:
        print("YBS-3 GRUBUNUN ETKİLEŞİM ORANI BAŞARISIIZ!!")


x = float(input("YBS-1 grubunun beğeni sayısını giriniz: "))
y = float(input("YBS-1 grubunun yorum sayısını giriniz: "))
z = float(input("YBS-1 grubunun paylaşım sayısını giriniz: "))
m = float(input("YBS-1 grubunun içerik sayısını giriniz: "))
n = float(input("YBS-1 grubunun takipçi sayısını giriniz: "))
k = float(input("YBS-2 grubunun beğeni sayısını giriniz: "))
a = float(input("YBS-2 grubunun yorum sayısını giriniz: "))
b = float(input("YBS-2 grubunun paylaşım sayısını giriniz: "))
c = float(input("YBS-2 grubunun içerik sayısını giriniz: "))
d = float(input("YBS-2 grubunun takipçi sayısını giriniz: "))
e = float(input("YBS-3 grubunun beğeni sayısını giriniz: "))
f = float(input("YBS-3 grubunun yorum sayısını giriniz: "))
g = float(input("YBS-3 grubunun paylaşım sayısını giriniz: "))
h = float(input("YBS-3 grubunun içerik sayısını giriniz: "))
l = float(input("YBS-3 grubunun takipçi sayısını giriniz: "))

eoHesapla(x, y, z, m, n)
eo2Hesapla(k, a, b, c, d)
eo3Hesapla(e, f, g, h, l)