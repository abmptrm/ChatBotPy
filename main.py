import sys
import random 
import os
from time import sleep

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")



print("""

- Pilih No 2 Terlebih Dahulu,
  Setelah Memasukan Nama -

""")

nama = input("Masukan Namamu: ")


lagiapa = random.choice([
    "Lagi duduk",
    "Lagi nugas :(",
    "Lagi makan",
    "Lagi eek hehe",
    "lagi nungguin dia :(", 
    "lagi kerja"
])

ketawa = random.choice([
    "Hahahahaha",
    "Wkwkwkwkwk",
    "Hehehehehe",
    "Xixixixixi",
    "hiyahiyahiya"
])

apaKabar = random.choice([
    "Sehat Alhamdulillah",
    "Aku sehat kok",
    "Sehat",
    "Alhamdulillah"

])

makanan = random.choice([
    "Aku suka Bakso",
    "Aku suka Sate",
    "Aku suka Ayam Goreng",
    "Aku suka Mie Goreng , Buka Miess u :v",
    "Aku suka Kamu hehehe :)"
])

akuJugaLope = random.choice([
    "Ahhh Melele Aku",
    "Makasih cayang",
    "Aku juga cuka kamu",
    "Terbang aku haaaaa"
    
])

minuman = random.choice([
    "Aku suka Es jeruk",
    "Aku suka Kopi Cappucinno",
    "Aku suka Es teh",
    "Aku suka Air Putih",
    "Aku suka kamu hehehe :)"
])

pantun = random.choice([

    """Ada jahe ada kencur
    Semua dicampur jadilah bumbu
    Beberapa hari ini aku susah tidur
    Karena selalu ingat dirimu""",
                
    """Beribu-ribu pohon beringin
    Hanya satu di pohon randu
    Saat malam terasa dingin
    Hanya wajahmu yang aku rindu""",
                
    """Jalan-jalan ke kebun
    Membeli buah nangka dan jambu
    Tak peduli dalam situasi apapun
    Saya tetap akan menemanimu"""         

])

help = "halo, hai, pantun, kamu lagi apa, lagi apa, siapa namaku, siapa namamu, apa kabar"

jawaban_user = {

    "p" : "Dilarang p",
    "halo" : "Halo juga " + nama ,
    "helo" : "Helo juga " + nama ,
    "assalamualaikum" : "waalaikumsalam",
    "hai" : "Hai juga " + nama,
    "hi" : "Hi juga " + nama,
    "makanan kesukaan kamu apa" : makanan,
    "makanan kesukaan" : makanan,
    "kamu suka makanan apa" : makanan,
    "minuman kesukaan kamu apa" : minuman,
    "minuman kesukaan" : minuman,
    "kamu suka minuman apa" : minuman,
    "aku juga suka kamu" : akuJugaLope,
    "siapa namamu" : "Namaku Bot",
    "siapa nama kamu" : "Namaku Bot",
    "nama kamu siapa" : "Namaku Bot",
    "siapa nama aku" : "Nama Kamu " + nama,
    "siapa namaku" : "Nama Kamu " + nama,
    "apa kabar" : "Alhamdulilah sehat",
    "pantun" : pantun,
    "!help" : help,
    "kamu lagi ngapain" : lagiapa,
    "kamu lagi apa" : lagiapa,
    "lagi apa" : lagiapa,
    "makan yang banyak ya" : "Udah kenyang",
    "semangat" : "Oke :)",
    "bau" : "Hoek",
    "iri" : "Bilang bos hahay bal bale bal bale",
    "stress" : "Asu",
    "oke" : "sip",
    "ketawa" : ketawa,
    "ketawa dung" : ketawa,
    "ketawa dong" : ketawa,
    "haha" : "Cie ketawa",
    "hahaha" : "Cie ketawa",
    "hahahaha" : "Cie ketawa",
    "wkwk" : "Cie ketawa",
    "wkwkwk" : "Cie ketawa",
    "wkwkwkwk" : "Cie ketawa",
    "xixi" : "Cie ketawa",
    "xixixi" : "Cie ketawa",
    "xixixixi" : "Cie ketawa",
    "hehe" : "Cie Ketawa",
    "hehehe" : "Cie Ketawa",
    "hehehehe" : "Cie Ketawa"

  }

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

def chatting():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    while True:
        kamu = input(nama + "\t: ") 

        if kamu.lower() in jawaban_user:
            print("Bot\t: "+ jawaban_user[kamu.lower()])
    
        else:
            print("Bot\t: Aku tidak paham")
            chatting()

def pake():

    if os.name == "nt":
        os.system("cls")
    else:   
        os.system("clear")

    print("Tunggu")
    sleep(2)

    if os.name == "nt":
        os.system("cls")
    else:   
        os.system("clear")

    print("""
- Tidak Mendukung Huruf Kapital
- Kecuali Pemasukan Namamu 
- Ketik "!help" di chatting
- Tidak Mendukung Simbol (?!.@#$%^&*_-=+|\,"';:~`)
- Pilih No 1 Untuk Memulai Chat -

-  Thank's  -


    """)


def screen_menu():

    if os.name == "nt":
        os.system("cls")
    else:   
        os.system("clear")

    print("""
+================+
|     ChatBot    |
+================+
| [1] Chatting   |
| [2] How to use |
| [0] Exit       |
+================+
    """)

    pilih_menu = int(input("Pilih\t: "))

    if pilih_menu == 1:
        sleep(2)
        chatting()

    elif pilih_menu == 2:
        pake()

        sleep(10)

        if os.name == "nt":
            os.system("cls")
        else:   
            os.system("clear")

        print("Tunggu")
        sleep(3)
        screen_menu()
        
    elif pilih_menu == 0:
        text = "bye "

        for i in range(10):
            print(text ,  end=" ")
            for a in range(i + 1):
                print(". " ,  end=" ")
                sleep(0.3)
                clear()
            print()

    else:
        print("error")
        sleep(2)
        screen_menu()

screen_menu()


    



