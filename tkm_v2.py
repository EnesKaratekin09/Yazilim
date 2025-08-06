import random
secim_listesi=["Taş","Kağıt","Makas"]
ts=0
ks=0
ms=0
os=0
oks=0
pcks=0
isim=input("Adınız nedir?\n")
print("Merhaba",isim)
def agirlik(t,k,m):
    agirlikli=max(t,k,m)
    return agirlikli
def counter(x):
    if x == ts:
        return "Kağıt"
    elif x == ks:
        return "Makas"
    elif x == ms:
        return "Taş"
    else:
        pc=random.choice(secim_listesi)
        return pc
def oyun():
     global ts, ks, ms, os, oks, pcks, pc, agirlikli
     while True:
        against = agirlik(ts, ks, ms)
        pc=counter(against)
        secim=input("\n\nTaşı seçmek için T\nKağıtı seçmek için K\nMakası seçmek için M yazınız.\nÇıkmak için q yazınız.\n").strip().upper()
        if secim not in ["T","K","M","Q"]:
            print("Geçersiz seçim.")
            continue
        if secim=="T":
            ts=ts+1
        elif secim=="K":
            ks=ks+1
        elif secim=="M":
            ms=ms+1
        elif secim=="Q":
            print("Kapatılıyor.")
            quit()
        #Taş,kağıt ve makas sayısı her oyunda sayılacak.
        if pc=="Taş" and secim=="K":
            kazanan="Kazandınız."
            oks=oks+1
        elif pc=="Taş" and secim=="M":
            kazanan="Bilgisayar kazandı."
            pcks=pcks+1
        elif pc=="Kağıt" and secim=="T":
            kazanan="Bilgisayar kazandı."
            pcks=pcks+1
        elif pc=="Kağıt" and secim=="M":
            kazanan="Kazandınız."
            oks=oks+1
        elif pc=="Makas" and secim=="K":
            kazanan="Bilgisayar kazandı."
            pcks=pcks+1
        elif pc=="Makas" and secim=="T":
            kazanan="Kazandınız."
            oks=oks+1
        else:
            kazanan="Berabere"
        os=os+1 
        print("Bilgisayar ",pc,"yaptı.\n")
        print(kazanan)
        print("Oyuncu {} - {} Bilgisayar" . format(oks,pcks))
        print(str(os))
oyun()
