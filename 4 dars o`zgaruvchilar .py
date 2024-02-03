# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:55:47 2024

@author: mirzo
"""

#ism = "Anvar"

#print ("Mening ismim " + ism)

ism = 'Ahad'
familiya = "Qayum"
print (ism+familiya)
print(ism+ ' '+familiya) 
ismsharif = f"{ism} {familiya}"
print(ismsharif)
print ("mening ismim"' '+ ismsharif)
print(f"Salom mening ismim, {ism} {familiya}")
print (f"mening ismin, {ism} \t{familiya}")  #\t belgisi uzun bushliq qoldiradi
print (f"mening ismim, \n{ism} \t{familiya}") #\n keyingi qatorga utadi


#metotlar
print (ism + familiya.upper())
print (ism.upper()+ ' ' +familiya.upper()+' ' + ismsharif.upper()) #.upper() xamma xarflarni katta xarfda yozadi
print(ism+familiya.lower())                                        #.lower() xamma xarfni kichik xarfda yozadi
print(ism.lower()+ ' '+familiya.lower())
print(ism.title()+familiya.title())                                #.title() bosh xarfni katta qiladi

meva = "     olma    "
print (meva)
print(meva.lstrip())          #matndan chap tarafdagi bushliqni olib tashlaydi
print(meva.rstrip())          #matndan ung tarafdagi bushliqni olib tashlaydi
print(meva.strip())           #matnning ikkala tarafidagi busgliqni olib tashlaydi
print ("men" ' ' +meva.strip()+ "ni juda yaxshi kuraman")

#INPUT

#ot = input("ismingiz\n>>>")
#ot2 = input("sizning ismingiz nima\n>>>")
#print("mening ismim" ' ' +ot)
#print("mening ismim" ' ' +ot.title() )
#print(ot2)
#print("sizning ismingiz" ' ' +ot2.title())


kucha = input(kuchda va uy raqamini kiriting)
tuman = input(tuman)
viloyat = input(viloyat)
print("siz" ' '+viloyat.title()"ti" ' '+tuman.title()"ni" ' '+kucha.title()"chi uyda yashaysizmi")
