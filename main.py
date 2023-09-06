from tkinter import *

window = Tk()
window.title("BMI Hesaplama")
window.minsize(width=400, height=300)


my_label = Label(text="Vücut Kitle Endeksi Hesaplama Aracı")
my_label.config(font=("Ariel", 10, "bold underline" )) #Başlığa alt çizgi koydum.
my_label.pack()

my_label2 = Label(text= "*Doldurulması zorunlu alanlar.")
my_label2.place(x=10, y=30)

my_label3 = Label(text= "*Cinsiyet")
my_label3.config
my_label3.place(x=10, y=60)
#
def cinsiyet_secimi():
    print(yapılan_secim.get())

yapılan_secim = IntVar()
erkek_secimi = Radiobutton(text="Erkek", value=0, variable=yapılan_secim, command=cinsiyet_secimi)
kadın_secimi = Radiobutton(text="Kadın", value=1, variable=yapılan_secim, command=cinsiyet_secimi)
erkek_secimi.place(x=70, y=60)
kadın_secimi.place(x=70, y=80)

my_label4 = Label(text="*Boyunuz(cm):")
my_label4.place(x=10, y=110)

my_label5 = Label(text="*Kilonuz(kg):")
my_label5.place(x=10, y=160)

def girilin_boy():

    try:
        a = int(my_entryboy.get())
        b = int(my_entry2kg.get())
        hata_mesaj.config(text="")
    except ValueError:
        hata_mesaj.config(text="Değer(ler), eksik veya yanlış! \nLütfen tekrar deneyiniz.")
    bmı = b / (a / 100 * a / 100)
    bmı3 = (f"{bmı:.2f}")
    bmı2 = "Sonuç:", bmı3
    label_sonuc.config(text=bmı2)


my_entryboy = Entry(width=10)
my_entryboy.place(x=20, y=135)

my_entry2kg = Entry(width=10)
my_entry2kg.place(x=20, y=185)


my_button = Button(text="Hesapla",command= girilin_boy)
my_button.config(font=("Ariel",10, "bold"))
my_button.config(padx=5, pady=5)
my_button.place(x=20, y=215)



label_sonuc = Label(text="", font=("Arial", 10, "bold" ))
label_sonuc.place(x=25, y=260)

bilgi_ekranı = Label(text="BİLGİ")
bilgi_ekranı.config(bg="light blue")
bilgi_ekranı.config(fg="white", font=("Ariel", 10, "bold"))
bilgi_ekranı.place(x=250, y=80)

bilgisonuclar_ = Label(text="10-18,15 / Zayıf \n18,5-25 / Sağlıkı \n25-30 / Kilolu \n30-40 / Şişman \n40-60 / Aşırı Şişman")
bilgisonuclar_.place(x=210, y=110)
bilgisonuclar_.config(bg="mint cream")
bilgisonuclar_.config(fg="black", font=("Ariel", 10, "bold"))

hata_mesaj = Label(text=" ")
hata_mesaj.place(x=20, y=250)

window.mainloop()

