# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:07:46 2024

@author: mirzo
"""

import random

def sontop(x=10):
    tasoddifiy_son = random.randint(1, x)
    print(f'Men 1 dan {x} gacha son o`yladim topa olasizmi?')
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input('>>>'))
        if taxmin<tasoddifiy_son:
            print('Xato. Men o`ylagan son bundan katta.')
        elif taxmin>tasoddifiy_son:
            print('Xato. Men o`ylagan son bundan kichik')
        else:
            break
    print(f'Tabkirlaymiz {taxminlar} ta taxmin bilan topdingiz topdingiz')
    return taxminlar
    


def sontop_pc(x=10):
    input(f'1 dan {x} gacha son o`ylang va istalgan tugmani bosin. Men topaman')
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1 
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f'Siz {taxmin} sonini o`yladingiz: to`g`ri (t),'
                      f'men o`ylagan son bundan kattaroq (+), yoki kichikroq (-)'.lower())
        if javob == '-':
            yuqori = taxmin - 1
        elif javob == '+':
            quyi = taxmin + 1
        else:
            break
    print(f'Topdim!!! Men {taxminlar} ta taxmin bilan topdim')
    return taxminlar
    
def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        if taxminlar_user>taxminlar_pc:
            print('Men yutdim')
        elif taxminlar_user<taxminlar_pc:
            print('Siz yutdingiz')
        else:
            print('DURRANG')
        yana = int(input('Yana o`ynaymizmi? HA(1) YO`Q(0)'))
            
play()
