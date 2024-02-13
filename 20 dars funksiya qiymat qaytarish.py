# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:39:44 2024

@author: mirzo
"""

# def tuliq_ism_yasa(ism, familiya):
#     """Tuliq ism familiya qaytaruvchi funksiya"""
#     tuliq_ism = f"{ism.title()} {familiya.title()}"
#     return tuliq_ism
    

# talaba = tuliq_ism_yasa('olim', 'asadov')
# print(talaba)

# def tuliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Tuliq ism familiya qaytaruvchi funksiya"""
#     if otasining_ismi:
#        tuliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#        tuliq_ism = f"{ism} {familiya}"
#     return tuliq_ism.title()
# talaba = tuliq_ism_yasa('olim', 'hakomov')
# print(talaba)


# def avto_info(kompaniya, model, rangi, karobka, yili, narxi=None):
#     """Avtomobillar haqida ma`lumot beradi"""
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rangi':rangi,
#             'karobka':karobka,
#             'yili':yili,
#             'narxi':narxi}
#     return avto
# avto1 = avto_info('GM', 'malubi', 'Qora', 'avtomat', '2023')
# avto2 = avto_info('BMW', 'x7', 'Oq', 'avtomat', '2022',15000)
# avtolar = [avto1, avto2]
# print(avtolar)
# for avto in avtolar:
#     if avto['narxi']:
#         narxi = avto['narxi']
#     else:
#         narxi = 'Nomalum'
#     print(f"{avto['rangi']} {avto['model']}. Narxi: {narxi}")
    
# def oraliq(min, max):
#     """sonlar"""
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(0, 10))
# print(oraliq(10, 21))


def oraliq(min, max, qadam):
    """sonlar"""
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += qadam
    return sonlar
print(oraliq(0, 10, 2))
print(oraliq(10, 30, 3))

def oraliq(min, max, qadam=1):
    """sonlar"""
    sonlar = []
    while min < max:
        sonlar.append(min)
        min += qadam
    return sonlar

print(oraliq(0, 10, 2))
print(oraliq(10, 30))

    