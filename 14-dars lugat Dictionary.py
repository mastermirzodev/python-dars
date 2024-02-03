# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:56:07 2024

@author: mirzo
"""

# car = {'model':'BYD','rang':'oq'}
# print(car['model'])
# print(car['rang'])

# en_uz = {'apple':'olma','apricot':'urik','banana':'banan',}
# print(en_uz['apple'])
# print(en_uz[input('suz kiriting\n>>>')])


mevalar = {'olma':12000,'uzum':22000,'nok':32000,'xurmo':42000}
meva = input('meva nomini kiriting\n>>>')
nmeva = mevalar.get(meva)
print(f"bozorda {meva}ning narxi {nmeva} so`m")  

# mukammal variant
if nmeva==None:
    print('Bozorda bunday meva yuq')
else:
    print(f'bozorda {meva}ning narxi {nmeva} so`m')




 # \ slesh bilan bir necha qator qilib yozish mumkin
 
# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-yilda tu'gilgan,\
#  {talaba_0['yosh']} yoshda")
 
# talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
# talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika' 
# print(talaba_0)

# ism ni almashtirish consolda kiritiladi
#  talaba_0['ism'] = 'abdullox'


# bush lugatga malumot yuklash

# talaba_1 = {}

# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# lugatdan malumotlarni uchirish  operator del

# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(talaba_0)
# del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
# print(talaba_0)

# agar lugat uzun bulsa qatorlarga bulib yozish mumkin
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
# print(telefonlar)
# #  get() METODI
# phone = telefonlar.get('hasan','Bunday ism mavjud emas')
# print(phone)



