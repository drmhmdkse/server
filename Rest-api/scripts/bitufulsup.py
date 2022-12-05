import requests
from bs4 import BeautifulSoup

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sozluk')

import django
django.setup()


from sozluk.models import Word


def kelimeTara(kelime:str):
    liste={}
    url = 'https://dictionary.cambridge.org/dictionary/english/'+kelime.rstrip()

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
        'referer':'https://www.google.com/'
    }

    response = requests.get(url,headers=header)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi,"html.parser")

    adjective_sifat=soup.find("div",attrs={"class":"pos-header dpos-h"})

    kelime= adjective_sifat.findChild()
    liste["kelime"]=kelime.text
    nitelik=adjective_sifat.find("div",attrs={"class":"posgram dpos-g hdib lmr-5"})
    liste["nitelik"]=nitelik.text
    usSoundLink=adjective_sifat.find("source",attrs={"type":"audio/mpeg"})
    liste["usSoundLink"]=usSoundLink.get("src")

    '''--------------------------------ikinci --------------------------'''

    alt_taraf=soup.find("div",attrs={"class":"sense-body dsense_b"})
    ikinci_div=alt_taraf.find("div",attrs={"class":"def-block ddef_block"})
    tanim=ikinci_div.find("div",attrs={"class":"def ddef_d db"}).text
    liste["description"]=tanim
    ilk_ornek_divi=soup.find("div",attrs={"class":"lbb lb-cm lpt-10"})
    ilk_ornek=ilk_ornek_divi.find("span").text.lstrip().rstrip()
    liste["example"]=ilk_ornek

    return liste


def save_islemi():
    with open("/home/durdu/Desktop/Rest-api/scripts/corncob_lowercase.txt",mode="r") as f:
        olmayanKelime=0
        kelimeler=f.readlines()
        for kelime in kelimeler:
            try:
                sonuc=kelimeTara(kelime)
                word=Word(name=sonuc.get("kelime"),description=sonuc.get("description"),voice=sonuc.get("usSoundLink"),partOfSpeech=sonuc.get("nitelik"),example=sonuc.get("example"))
                word.save()

            except:
                olmayanKelime += 1
                print("bu kelimenin meali yok hocam : "+kelime)


        print(olmayanKelime)
