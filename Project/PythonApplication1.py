import module
import sqlite3
aracBoya=1
aracTur=0
tcNo=0 
boyaMaliyet=1000
geneListe=[]
cikis=1
liste=[]
sistemCikis=5
sozluk={}
sayac=0
kamyon=0
otomobil=0
otobüs=0
Vliste=[]
ToplamKazanc=0

veritabanı=sqlite3.connect('MusteriKayitlari.db')
imlec=veritabanı.cursor()
Tablo="""CREATE TABLE IF NOT EXISTS 
Musteriler (Ad,Soyad,tcNO,telNO,Arac,Plaka,Ucret)"""
imlec.execute(Tablo)

print("""

//Yagiz Pasha Tune Shop'a Hosgeldiniz//

""")
print("Asagidaki menuden taleplerinizi ilettikten sonra robotlar arabanıza sectiginiz islemleri yapacaktir. \n")   
while(sistemCikis==5):
    
    sayac=sayac+1
    sListe=[]
    ucret=0
    k_cikis=1
    cikis=1
    aracSorgu=5
    tcSorgu=5
    #Ad=input("Adınızı giriniz : ")
    #Soyad=input("soyad giriniz : ")
    class Kisi():
        Ad=""
        Soyadi=""
    nesne=Kisi()
    nesne.Ad=input("Müşterinin adınızı giriniz : ")
    nesne.Soyad=input("Müşterinin soyadını giriniz : ")
    
    
    #
    tcNo=module.tcAlma()
    
    tel_sorgu=1
    while(tel_sorgu==1):
        try:
            tel_No=str(input("Telefon numarası giriniz : "))
            if len(tel_No)==10:
                tel_sorgu=2
            else:
                print("Lütfen başında 0 olmadan telefon numaranızı düzgün giriniz.")
        except:
            print("hata!")



    plaka=input("Plakanızı girin.  :   ")


    

    while(aracSorgu==5):
        try :   
            aracTur=int(input("""Araciniz Otomobil ise 1 : 
             Kamyon ise   2 :
             Otobüs ise   3 :
            """))
            if (aracTur==1):
                  otomobil=otomobil+1
                  aractur="otomobil"
                  aracBoya=boyaMaliyet*1
                  aracSorgu=8
            elif (aracTur==2):
                    kamyon=kamyon+1
                    aractur="kamyon"
                    aracBoya=boyaMaliyet*2
                    aracSorgu=8
            elif (aracTur==3):
                    otobüs=otobüs+1
                    aractur="otobüs"
                    aracBoya=boyaMaliyet*3
                    aracSorgu=8
        except:
           print("hata !")

         
         
    while (cikis==1):
    
        secim=int(input("""
----------------------------------------------------------------------
        1--)Yag Degisimi

        2--)DYNO Testi

        3--)Yıllık Bakıma Uygunluk Testi

        4--)Modifiye

        5--)Kullanicidan Cikis
----------------------------------------------------------------------
        """))     
    
        if secim==1:
           print("Yag degisiminizle robotlarimiz ilgilenecektir.")
           ucret=ucret+250
        elif secim==2:
            print("DYNO testiyle robotlarimiz ilgilenecektir")
            ucret=ucret+100
        elif secim==3:
            egDurum=input("Egzoz'da beyaz/siyah/mavi yoğunlukta duman var mı? Varsa (e/h) : ")
            if (egDurum=='e'):
                print("Motor yağ yakıyor olabilir, Motorun içine su giriyor, Egzoz partikul filtreleyici sorunlu olabilir. \n")
                bakim=1
                while(bakim==1):  
                    secim=int(input("""
                    1-Yag yakmayi kontrol ettirmek
                    2-Su kacagi kontrol ettirmek
                    3-Egzoz partikül filtreleyici değisimi
                    4-Bakim menüsünden cikis
                    """))
                    if secim==1:
                        ucret=ucret+100
                    elif secim==2:
                        ucret=ucret+100
                    elif secim==3:
                        ucret=ucret+250
                    elif secim==4:
                        bakim=3
        elif secim==4:
            ucret+=module.secim4(aracBoya)
        elif secim==5:
            while (k_cikis==1):
                    try:
                        eminOlmak=str(input("Kullanicidan cikmak istediginize emin misiniz? (e/h) : "))
                        if eminOlmak=='e':
                            cikis=3
                            k_cikis=2
                        elif eminOlmak=='h':
                            cikis=1
                            k_cikis=2
                    except:
                        print("Gecerli bir harf girin.")
                        print("\a")
    
    geneListe=[nesne.Ad,nesne.Soyad,tcNo,tel_No,aractur,plaka,ucret]
    liste.append(geneListe)
    cikis=input("""
    1- Sistemden Cikis yapicak misiniz? (e/h)
    """)
    sis_cikis=1
    adSoyad=nesne.Ad+" "+nesne.Soyad
    sListe=[nesne.Ad,nesne.Soyad,tcNo,tel_No,aractur,plaka,ucret]
    sozluk.setdefault(adSoyad,sListe)
    ToplamKazanc=ToplamKazanc+ucret
    
    while(sis_cikis==1): 
        try:
                           
            if cikis=='e':
                    sis_cikis=2    
                    sistemCikis=8
            elif cikis=='h':
                    sis_cikis=2
        except:
            print("hata !")
    

    Vliste=[nesne.Ad,nesne.Soyad,tcNo,tel_No,aractur,plaka,ucret]      
    nesne.Ad=str(nesne.Ad)    
    nesne.Soyad=str(nesne.Soyad)   
    tcNo=str(tcNo)    
    tel_No=str(tel_No)    
    aractur=str(aractur)    
    plaka=str(plaka)    
    ucret=str(ucret)
    imlec.execute("""INSERT INTO Musteriler VALUES   (?, ?, ?, ?, ?, ?, ?)""", Vliste)
    veritabanı.commit()
    

module.gunSonuRaporu(liste)

vt="e"
while(vt=="e"):    
    vti=input("Veritabanından sorgu yapmak için (e/h)")
    if vti=="e":
        vtTC=input("Arama icin TC numarasi giriniz : ")
        imlec.execute("""SELECT * FROM Musteriler WHERE  tcNo = '%s' """%(vtTC))
        data=imlec.fetchone()
        print(data)
    elif vti=="h":
        vt="5"
    else:
        print("???")
module.arama(sayac,sozluk)
otomobil1=otomobil
kamyon1=kamyon
otobüs1=otobüs
toplamVasıta=otomobil+kamyon+otobüs
otomobil="Otomobil"+" "+str(otomobil)
kamyon="Kamyon"+" "+str(kamyon)
otobüs="Otobüs"+" "+str(otobüs)
Vliste=[otomobil,kamyon,otobüs,toplamVasıta,ToplamKazanc]
Vsozluk={"Muayne Olan Vasıta Sayısı":
         {"Otomobil":otomobil1,
          "Kamyon":kamyon1,
          "Otobüs":otobüs1,
          "Toplam Vasıta":toplamVasıta,
          "Toplam Kazanç":ToplamKazanc}
         }
       

#Vsozluk.setdefault("MuayneOlanVasıtaSayısı",Vliste)

print(Vsozluk)