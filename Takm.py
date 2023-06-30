import random
import sqlite3
pcskor=0
oyuncuskor=0
ts=0
ks=0
ms=0
secim_listesi=["Taş","Kağıt","Makas"]
#try:
conn=sqlite3.connect('taskagitmakas.db')
isim=input("Adınız nedir?\n")
print("Merhaba",isim)
crt="""CREATE TABLE IF NOT EXISTS oyuncu (NAME CHAR(25),TAS_SAYISI VARCHAR(5),KAGIT_SAYISI VARCHAR(5),MAKAS_SAYISI VARCHAR(5));"""

cursor=conn.cursor()
cursor.execute(crt)
    
#except:
#    print("Hata oluştu.")

def oyun():
    secim=input("\n\nTaşı seçmek için T\nKağıtı seçmek için K\nMakası seçmek için M\nÇıkmak için Ç yazınız.\n")
    pc=random.choice(secim_listesi)
    global pcskor, oyuncuskor, ts, ks, ms
    if pc=="Taş" and secim=="K":
        kazanan="Kazandınız."
        oyuncuskor = oyuncuskor +1
        ks+=1
        print("Bilgisayar ",pc,"yaptı.\n")
        print(kazanan)
        print("Bilgisayar ",pcskor,":",oyuncuskor," ",isim)
        oyun()
    elif pc=="Taş" and secim=="M":
        kazanan="Bilgisayar kazandı."
        pcskor = pcskor +1
        ms+=1
        print("Bilgisayar ",pc,"yaptı.\n")
        print(kazanan)
        print("Bilgisayar ",pcskor,":",oyuncuskor," ",isim)
        oyun()
    elif pc=="Kağıt" and secim=="T":
        kazanan="Bilgisayar kazandı."
        pcskor = pcskor +1
        ts+= 1
        print("Bilgisayar ",pc,"yaptı.\n")
        print(kazanan)
        print("Bilgisayar ",pcskor,":",oyuncuskor," ",isim)
        oyun()
    elif pc=="Kağıt" and secim=="M":
        kazanan="Kazandınız."
        oyuncuskor = oyuncuskor +1
        ms+=1
        print("Bilgisayar ",pc,"yaptı.\n")
        print(kazanan)
        print("Bilgisayar ",pcskor,":",oyuncuskor," ",isim)
        oyun()
    elif pc=="Makas" and secim=="K":
        kazanan="Bilgisayar kazandı."
        pcskor = pcskor +1
        ks+=1
        print("Bilgisayar ",pc,"yaptı.\n")
        print(kazanan)
        print("Bilgisayar ",pcskor,":",oyuncuskor," ",isim)
        oyun()
    elif pc=="Makas" and secim=="T":
        kazanan="Kazandınız."
        oyuncuskor = oyuncuskor +1
        ts+=1
        print("Bilgisayar ",pc,"yaptı.\n")
        print(kazanan)
        print("Bilgisayar ",pcskor,":",oyuncuskor," ",isim)
        oyun()
    elif pc=="Taş"and secim=="T":
        kazanan="Berabere."
        ts+=1
        print("Bilgisayar ",pc,"yaptı.\n")
        print(kazanan)
        print("Bilgisayar ",pcskor,":",oyuncuskor," ",isim)
        oyun()
    elif pc=="Kağıt" and secim=="K":
        kazanan="Berabere."
        ks+=1
        print("Bilgisayar ",pc,"yaptı.\n")
        print(kazanan)
        print("Bilgisayar ",pcskor,":",oyuncuskor," ",isim)
        oyun()
    elif pc=="Makas" and secim=="M":
        kazanan="Berabere."
        ms+=1
        print("Bilgisayar ",pc,"yaptı.\n")
        print(kazanan)
        print("Bilgisayar ",pcskor,":",oyuncuskor," ",isim)
        oyun()
    elif secim=="Ç":
        print("Çıkış yaptınız , iyi günler dileriz.")
        ins="""INSERT INTO oyuncu (NAME,TAS_SAYISI,KAGIT_SAYISI,MAKAS_SAYISI) VALUES ('{}','{}','{}','{}');""".format(isim,ts,ks,ms)
        cursor.execute(ins)
        #slct="""SELECT * FROM oyuncu;"""
        #cursor.execute(slct)
        #sec=cursor.fetchone()
        
        conn.commit()
        conn.close()
    else:
        print("Lütfen seçiminizi belirtin.")
        oyun()
    
        

oyun()


