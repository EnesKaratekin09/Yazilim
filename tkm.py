import random
secim_listesi=["Taş","Kağıt","Makas"]
isim=input("Adınız nedir?\n")
print("Merhaba",isim)
def oyun():
    while True:
        secim=input("\n\nTaşı seçmek için T\nKağıtı seçmek için K\nMakası seçmek için M yazınız.\n")
        pc=random.choice(secim_listesi)
        if pc=="Taş" and secim=="K":
            kazanan="Kazandınız."
        elif pc=="Taş" and secim=="M":
            kazanan="Bilgisayar kazandı."
        elif pc=="Kağıt" and secim=="T":
            kazanan="Bilgisayar kazandı."
        elif pc=="Kağıt" and secim=="M":
            kazanan="Kazandınız."
        elif pc=="Makas" and secim=="K":
            kazanan="Bilgisayar kazandı."
        elif pc=="Makas" and secim=="T":
            kazanan="Kazandınız."
        else:
            kazanan="Berabere"
        print("Bilgisayar ",pc,"yaptı.\n")
        print(kazanan)
oyun()
