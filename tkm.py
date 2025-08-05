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
def oran_yorumla(a,b,c): #En yüksek oranlı seçimin tersi 5/10, en az oranlı seçimin tersi 2/10 ihtimalle seçilecek.
    if max(a,b,c)==a and min(a,b,c)==c:
        yeni_liste=["Taş"]*2 + ["Kağıt"]*5 + ["Makas"]*3
    elif max(a,b,c)==a and min(a,b,c)==b:
        yeni_liste=["Taş"]*3 + ["Kağıt"]*5 + ["Makas"]*2
    elif max(a,b,c)==b and min(a,b,c)==a:
        yeni_liste=["Taş"]*3 + ["Kağıt"]*2 + ["Makas"]*5
    elif max(a,b,c)==b and min(a,b,c)==c:
        yeni_liste=["Taş"]*2 + ["Kağıt"]*3 + ["Makas"]*5
    elif max(a,b,c)==c and min(a,b,c)==a:
        yeni_liste=["Taş"]*5 + ["Kağıt"]*2 + ["Makas"]*3
    elif max(a,b,c)==c and min(a,b,c)==b:
        yeni_liste=["Taş"]*5 + ["Kağıt"]*3 + ["Makas"]*2
    else:
        yeni_liste=["Taş","Kağıt","Makas"]
    return yeni_liste
def oyun():
     global ts, ks, ms, os, oks, pcks, secim_listesi
     while True:
        if os % 10 == 0 and os != 0: #Oyun sayısı 10'un katlarındaysa oran yorumlama fonksiyonu çalışıp AI'a komut verecek.
            secim_listesi = oran_yorumla(ts, ks, ms)
        secim=input("\n\nTaşı seçmek için T\nKağıtı seçmek için K\nMakası seçmek için M yazınız.\n").strip().upper()
        pc=random.choice(secim_listesi)#İlk 10 oyunda rastgele seçim yapacak.
        if not secim=="T" and not secim=="K" and not secim=="M":
            print("Geçersiz seçim.")
            oyun()
        if secim=="T":
            ts=ts+1
        elif secim=="K":
            ks=ks+1
        elif secim=="M":
            ms=ms+1
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
