# -*- coding: utf-8 -*-
# !/usr/bin/env python
import requests,time
import sys,os
os.system("clear")

x="""
 ██████╗ ███╗   ██╗ ██████╗
██╔════╝ ████╗  ██║██╔════╝
██║  ███╗██╔██╗ ██║██║     
██║   ██║██║╚██╗██║██║     
╚██████╔╝██║ ╚████║╚██████╗
 ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝
                           
Sistem baslatiliyor... (Versiyon: 1)
%s
"""%("-"*40)
print(x)

base_url="https://gnc-yeni.herokuapp.com/"


def lisans_kontrol(username):
        url="https://gnc-yeni.herokuapp.com/lisans_kontrol"
        s=requests.get(url,params={"username":username}).text
        print("Lisans kontrolü: %s  tarihine kadar"%s)
        if s=="False":
            print("Lisans için iletişime geçin...")
            sys.exit()


if requests.get(base_url).text=="OK":
    print("Sistem Açık!\n")
    username=input("Numara: (başında sıfır olmadan, bitişik)\n>")
    lisans_kontrol(username)
    print("%s\n%s için işlem yapılacak\n"%("-"*45,username))
    password=input("Şifre:\n")
    sor1=input("%s\n1.Çoklu çatlat  2.Gün değiştir\nHangi işlem?\n"%("-"*45))
    if sor1=="1":
        count=input("Kaç defa:\n")
        pyld={
          "username":username,
          "password":password,
          "count":count,   
        }
        r1=requests.post(base_url+"gnc_basla",json=pyld)
        print(r1.text)
        print("Çıkış yapılacak...")
        time.sleep(10)
        sys.exit()
    elif sor1=="2":
        pyld={
          "username":username,
          "password":password,
        }
        r1=requests.post(base_url+"gnc_gun",json=pyld)
        print(r1.text)
        time.sleep(10)
        sys.exit()
else:
    print("Sistem Açık Değil!")
    time.sleep(10)
    sys.exit()
    
