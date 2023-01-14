import matplotlib.pyplot as plt
import pandas as pd
 
class Grafik:
  def __init__(self,urun_turu, datalar):
    self.urun_turu = urun_turu
    self.datalar = datalar
  def Grf_show(self):
    self.datalar.head()
    plt.figure(figsize=(12,6))
    plt.plot(self.datalar.tarih,self.datalar[self.urun_turu]) # renk otomatik belirlenir       
    plt.title("2013'ten 2020'ye kadar olan yıllarda "+self.urun_turu+" ürünleri gelirleri")
    plt.xlabel("Tarih")
    plt.ylabel(self.urun_turu)
    plt.show()

# تابع لعمل تسجيل الدخول
def login(username,password):
    USERNAME='ahmed'
    PASSWORD='123'
    if USERNAME==username and PASSWORD==password:
        return True
    else:
        return False    

def switch(value):
    if value == 1:
        return "tarim"
    elif value == 2:
        return "Madencilik"
    elif value == 3:
        return "İmalat_sanayi"
    elif value == 4:
        return "Gıda"
    elif value == 5:
        return "İçecekler"
    elif value == 6:
        return "Tütün"
    elif value == 7:
        return "Tekstil"
    elif value == 8:
        return "Giyim"
    elif value == 9:
        return "Kağıt"
    elif value == 10:
        return "Kok"
    elif value == 11:
        return "Kimyasallar"
    elif value == 12:
        return "eczacılık"
    elif value == 13:
        return "Mobilya"


# تابع لتنفذ الرسم البياني
def urunlere_gore_sec(urun):
    try:
        data=pd.read_excel("excel1.xlsx")
        #veri tipinin floata çevrilmesi
        urun_adi=switch(urun)
        data[urun_adi] = data[urun_adi].astype('float')
        grafik=Grafik(urun_adi,data)
        grafik.Grf_show()
    except:
        print("hata uluştu ...")  
# هون الجزء الرئيسي
username = input('kullancı adı giriniz:\n')
password = input('şifre giriniz:\n')
while not login(username,password):
    print('kullancı adı ya da şifre yanlıştır')
    username = input('kullancı adı giriniz:\n')
    password = input('şifre giriniz:\n')

while True:
    print('---------------------------------------------------')
    print('0 ==> Çıkış için') 
    print('1 ==> başka bir işlem yapınız') 
    islem = input('seçeneğinizi giriniz\n')
    if int(islem)==0:
        print("Program sonlandırıldı")
        break
    elif int(islem)==1:
        print('---------------------------------------------------')
        print('bir ürün seçiniz ')
        print('1 ==> tarim')
        print('2 ==> Madencilik')
        print('3 ==> İmalat_sanayi')
        print('4 ==> Gıda')
        print('5 ==> İçecekler')
        print('6 ==> Tütün')
        print('7 ==> Tekstil')
        print('8 ==> Giyim')
        print('9 ==> Kağıt')
        print('10 ==> Kok')
        print('11 ==> Kimyasallar')
        print('12 ==> eczacılık')
        print('13 ==> Mobilya')
        sec = input('bir numara siçiniz?\n')
        urunlere_gore_sec(int(sec))
