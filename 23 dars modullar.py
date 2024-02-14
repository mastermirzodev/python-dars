# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:49:15 2024

@author: mirzo
"""
### 24 dars lambda funksiyasi 

# from math import sqrt

# sonlar = list(range(11))
# ildiz = list(map(sqrt, sonlar))
# print(ildiz)

# def daraja2(x):
#     return x*x
# print(list(map(daraja2, sonlar)))

# kvadrat = list(map(lambda x:x*x, sonlar))
# print(kvadrat)

# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)
# print(kvadratlar)

# a=[4,5,6,]
# b = [7,8,9,]
# a_plus_b = list(map(lambda x,y:x+y,a,b))
# print(a_plus_b)

import random as r

# sonlar = r.sample(range(100),10)
# print(sonlar)
# def juftmi(x):
#     return x%2==0

# juft_sonlar = list(filter(juftmi, sonlar))
# print(juft_sonlar)

# juft_sonla = list(filter(lambda x: x%2==0,sonlar))
# print(juft_sonla)

mevalar = ['olma','anor','urik','banan','tarvuz','qovun','anjir','danak']
harf = 'd'
mevalar_b = list(filter(lambda meva:meva.startswith(harf), mevalar))
print(mevalar_b)

mevalar2 = list(filter(lambda meva:len(meva)>=5, mevalar))
print(mevalar2)

mevalar3 = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
print(mevalar3)



