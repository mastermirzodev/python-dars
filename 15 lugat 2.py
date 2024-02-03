# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 21:18:46 2024

@author: mirzo
"""

#.items() METODI
# Ushbu metod yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin. 
# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }

# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f'kalit: {kalit}')
#     print(f'Qiymat: {qiymat} \n')


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
# for k, q in telefonlar.items():
#     print(f'{k.title()}ning telefoni {q}')

# .keys() METODI
# Agar lug'atdagi kalit so'zlarni ko'rish talab qilinsa, .keys() metodidan foydalanishimiz mumkin.
# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# print(mahsulotlar.keys())

# print('Do`kondagi maxsulotlar')
# for maxsulot in mahsulotlar.keys():
#     print(maxsulot.title())
    
# print('Do`kondagi maxsulotlar')
# for maxsulot in mahsulotlar:
#     print(maxsulot.title())

# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")
        
# print("Do'konimizdagi mahsulotlar:")    
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
# for m in mahsulotlar.values():
#     print(m)

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)
# set() funktsiyasi ruyxatdan bir turdagi maxsulotlarning faqat bittasini nomini kursatadi

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)
