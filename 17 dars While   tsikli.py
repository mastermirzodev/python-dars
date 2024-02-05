# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:05:48 2024

@author: mirzo
"""

# ism = input('Ismingiz nima:\n')
# savol = f"Salom, {ism.title()} Yoshingiz nechchida?\n"
# yosh = input(savol)
# yosh = int(yosh)
# buy = input('Buyingiz necha metr?')
# buy = float(buy)


# While()  takrorlash operatori (While: so`zining ma`nosi TOKI degan ma`noni bildiradi

# son = 1  # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan
#     print(son, end=' ') # son ni konsolga chiqaramiz
#     son += 1     # son ga 1 ni qo`shamiz
# print('Dastur tugadi')
    
# son = 1  # son ga 1 qiymatini beramiz
# while son<=int(input('son kiriting')): # toki son  dan kichik yoki teng ekan
#     print(son, end=' ') # son ni konsolga chiqaramiz
#     son += 1     # son ga 1 ni qo`shamiz


# print('Kiritilgan sonning kvadratini topadi')
# savol = "Istalgan sonni kiriting"
# savol += "(dasturni to`xtatish uchun 'exit' deb yozing):"  # exit o`rniga chiqish deb yozsakxab bo`ladi
# qiymat = ''
# while qiymat != 'exit':    # !=  teng bulmasa ma`nosini beradi
#     qiymat = input(savol)
#     if qiymat != 'exit':    # exit o`rniga xoxlagan so`z yozsak bo`ladi
#         print(float(qiymat)**2)
# print('Dastur tugadi')

# # ishora 
# print('Kiritilgan sonning kvadratini topadi')
# savol = "Istalgan sonni kiriting"
# savol += "(dasturni to`xtatish uchun 'exit' deb yozing):"  # exit o`rniga chiqish deb yozsakxab bo`ladi
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi')

# # break  while    # 

# print('Kiritilgan sonning kvadratini topadi')
# savol = "Istalgan sonni kiriting"
# savol += "(dasturni to`xtatish uchun 'exit' deb yozing):"  # exit o`rniga chiqish deb yozsakxab bo`ladi

# while True:    #  avadiy tsikl to`xtamasdan davom etadi
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break             # break bo`lsa yani exit qiymat kiritilsa tsikl to`xtatiladi
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi')

# # break fot tsikli uchun qo`llanishi
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f'{son} ning kavdrati {son**2} ga teng ')
    
# # continue  
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue    # bajarmasdan davom etish uchun ishlatiladi
#     print(f'{son} ning kavdrati {son**2} ga teng ')

# son = 0
# while son<10:
#     son += 1
#     if son%2!=0: # %2 = agar son 2 ga bo`linsa !=  sonning juft ekanligini tekshiradi  == bo`lsa toq ekanl;igini tekshiradi
#         continue
#     else:
#         print(son)
# son = 0
# while son<10:
#     son += 1
#     if son%2==0: # !=  sonning juft ekanligini tekshiradi  == bo`lsa toq ekanl;igini tekshiradi
#         continue
#     else:
#         print(son)




"""AMALIYOT"""
""" 1- mashq"""
"""Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating"""

# kitoblar = 'Yaxshi ko`rgan kitoblaringizni kiriting'
# kitoblar += '(kiritib bo`lgach "stop" deb yozing)'
# while True:
#     kitob = input(kitoblar)  
#     if kitob == 'stop':
#       break
# print('raxmat')

#  2- mashq
# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

# yosh = "Yoshingiz nechchida?\n"

# while True:
#     qiymat = int(input(yosh))
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     ysh = int(qiymat)
#     if ysh<7: 
#         narx = 2000
#     elif 7<=ysh<18:
#         narx = 3000
#     elif 18<=ysh<65:
#         narx = 10000
#     else:
#         narx = 0
#     if narx==0:
#         print("Sizga bepul")
#     else:
#         print(f'Sizga chipta narxi {narx} sum')
# print('Dastur tugadi')





# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "



# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")













    
