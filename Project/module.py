def tcAlma():  
    tcno=0
    tcSorgu=5
    while(tcSorgu==5):
    

                tcno=str(input("T.C.  Kimlik Numaranızı Giriniz : "))
                if len(tcno)==11:
                    if tcno.isdigit():
                        if not int(tcno)==0:
                            tcSorgu=7
                else:
                    print("\a")
                    print("\n *Lutfen T.C. numaranizin 11 haneli olmasina özen gösteriniz. *")
    return tcno


def secim4(aracBoya):
    ucret=0
    secim=int(input("""
            1-Boya
            2-Motor değiştirme
            3-Kanat ekleme
             """))
    if secim==1:
                secim=int(input("""
                Genel boyama arac cinsine göre degisiklik göstermektedir  
                arac icin 1000₺
                kamyon icin 2000₺
                otobüs icin 3000₺          
                1-Sarı
                2-Mavi
                3-Beyaz
                4-Yeşil           
                5-Cikis          
                """))
                if secim==1 or secim==2 or secim==3 or secim==4:
                    ucret=ucret+aracBoya
                    print("{} ucret hesabiniza yansitilacaktir.".format(aracBoya))
                elif secim==5:
                    print(" ")
    elif secim==2:
                    secim=input("""Elimizde 1 cesit motor var 
                    Sıralı 6 silindir 470 bg CL280 Mercedes motoru 49.000 ₺'dir.
                    Degistirmek ister misiniz? (e/h) :""")
                    if secim=='e':
                        ucret=ucret+49000          
    elif secim==3:
                secim=int(input("Kanat .HKS Super Bird.  mevcuttur. 4360₺ istiyorsanız (e/h) : "))
                if secim=='e':
                    ucret=ucret+4360
    return ucret


def gunSonuRaporu(liste):
    for i in range(len(liste)):
        print(""" 
        Gün Sonu Raporu
        Ad : {} 
        Soyad : {}
        T.C. NO : {}
        Tel. NO : {}
        Arac Turu: {}
        Plaka : {}
    
        Ucret : {} ₺
    
        """.format(liste[i][0],liste[i][1],liste[i][2],liste[i][3],liste[i][4],liste[i][5],liste[i][6]))



def arama(sayac,sozluk):
   t=1
   while(t==1):
       sorgu=input("Gecmis musteri kaydini sorgulamak istiyor musun? (e/h) (Sozlukten): ")
       k=1
       if sorgu=='e':
           if (sayac>1):
                musteriArama=input("""Isme göre arama yapacaksiniz. 
                Lutfen ismi dogru girmeye özen gösterin. 
                Ornek 'Ege Yagiz'  \n\n""")
                while (k==1):
                    
                            girdi=input("kimi arayacaksınız : ")
                            print(sozluk.get(girdi,"Müşteri bilgisine ulaşılamadı...Ismini düzgün yazdığınızdan emin olunuz."))
                            k=2
                    
                    
           elif sayac==1:
                print("Musteri sayisi 1'den büyük olmadığından arama yapamazsınız.")
                t=2
           
           else:
               print("Yanlis bastiniz ...")
       elif sorgu=='h':
           t=2
       else:
           print("Dogru komutu giriniz... ")






