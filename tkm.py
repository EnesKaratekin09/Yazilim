import random
secim_listesi=["Taş","Kağıt","Makas"]

def oyun():
    ugur=random.choice(secim_listesi)
    enes=random.choice(secim_listesi)
    if ugur=="Taş" and enes=="Taş":
        kazanan="Berabere."
    if ugur=="Taş" and enes=="Kağıt":
        kazanan="Enes kazandı."
    if ugur=="Taş" and enes=="Makas":
        kazanan="Uğur kazandı."
    if ugur=="Kağıt" and enes=="Taş":
        kazanan="Uğur kazandı."
    if ugur=="Kağıt" and enes=="Kağıt":
        kazanan="Berabere."
    if ugur=="Kağıt" and enes=="Makas":
        kazanan="Enes kazandı."
    if ugur=="Makas" and enes=="Taş":
        kazanan="Enes kazandı."
    if ugur=="Makas" and enes=="Kağıt":
        kazanan="Uğur kazandı."
    if ugur=="Makas" and enes=="Makas":
        kazanan="Berabere."
    
    print("Uğur:",ugur)
    print("Enes:",enes)
    print(kazanan)
    
    tekrar=input("")
    if tekrar=="":
        oyun()
oyun()
