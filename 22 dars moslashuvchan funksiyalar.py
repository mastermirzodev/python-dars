# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 20:30:17 2024

@author: mirzo
"""

# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(10,11,12,13,14,15,16,18))


# def summa(x,y,*sonlar):
#     return x+y+sum(sonlar)

# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(10,11,12,13,14,15,16,18))
      
      
      
# def avto_info(kompaniya,model,**malumotlar):
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1 = avto_info('gm','malubi',rang='oq',yil=2023,karobka='avtomat')
# avto2 = avto_info('kia','k5',rang='qora',narx='35000',yil=2024)
# avto =[avto1,avto2]
# print(avto)

def talaba_info(ism,familiya,**malumotlar):
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar
talaba1 = talaba_info('nazar','avazov',kurs=2,fakultet='informatika')
talaba2 = talaba_info('olim','hakimov',yil=2003,universitut='tatu',fakultet='avtomatika')
print(talaba1)
print(talaba2)