# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:47:04 2024

@author: mirzo
"""
#for takrorlash 
# mehmonlar = ["ali", "vali", "qosim", "nasiba", "malika", "dilnura", "olim"]
# for mehmon in mehmonlar:
#     print("Salom", mehmon)
#     print(f"Hurmatli {mehmon.title()}, sizni katta bazmga taklish etamiz \nHurmat bilan jamoa")
# print("Hayir", mehmon)

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
    
# print(sonlar)
# print(sonlar_kvadrati)

# dustlar = []
# print("5 ta eng yaqin dustingizni kiriting")
# for n in range(5):
#     dustlar.append(input(f"{n+1} dustingizni ismini kiriting:"))

# print(dustlar)


# ismlar = ["ali", "vali", "nabi", "alo", "rano"]
# for ism in ismlar:
#     print("Salom", ism)
# print(f"kod {len(ismlar)} marta takrorlandi.")

# toqs = list(range(11,100,2))
# for kub in toqs:
#     print(kub**3)

# kino = []
# print("5 ta kinoni kiriting")
# for k in range(5):
#     kino.append(input(f"{k+1} kinoni kiriting"))
# print(kino)


# suxbatlar = []
# input("bugun necha kishi bilan suxbat qildingiz")
# for sux in range(5):
#     suxbatlar.append(input(f"{sux+1} - suxbatdoshingizni kiriting::"))

# print(f"siz bugun {suxbatlar}, lar bilan uchrashdizgiz")

n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)