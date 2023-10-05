

'''
1. ¬Niño(Scrooge) ∨ Ama(Scrooge,PapáNoel)
2. ¬Ama(Scrooge,PapáNoel) ∨ ¬Reno(Rodolfo) ∨ Ama(Scrooge,Rodolfo)
3. Reno(Rodolfo)
4. NarizRoja(Rodolfo)
5. ¬NarizRoja(Rodolfo) ∨ Raro(Rodolfo) ∨ Payaso(Rodolfo)
6. ¬Reno(Rodolfo) ∨ ¬Payaso(Rodolfo)
7. ¬Raro(Rodolfo) ∨ ¬Ama(Scrooge,Rodolfo)

¬Niño(Scrooge)?
'''

ejemplo1 = {
    'clausulas': [
        '¬Niño(Scrooge) ∨ Ama(Scrooge,PapáNoel)',
        '¬Ama(Scrooge,PapáNoel) ∨ ¬Reno(Rodolfo) ∨ Ama(Scrooge,Rodolfo)',
        'Reno(Rodolfo)',
        'NarizRoja(Rodolfo)',
        '¬NarizRoja(Rodolfo) ∨ Raro(Rodolfo) ∨ Payaso(Rodolfo)',
        '¬Reno(Rodolfo) ∨ ¬Payaso(Rodolfo)',
        '¬Raro(Rodolfo) ∨ ¬Ama(Scrooge,Rodolfo)'
    ],
    'pregunta': '¬Niño(Scrooge)'
}

'''
1. Hombre(Marco)
2. Pompeyano(Marco)
3. ¬Pompeyano(Marco) ∨ Romano(Marco)
4. Gobernante(Cesar)
5. ¬Romano(Marco) ∨ Leal(Marco,Cesar) ∨ Odia(Marco,Cesar)
6. ¬Hombre(Marco) ∨ ¬Gobernante(Cesar) ∨ ¬IntentaAsesinar(Marco,Cesar) ∨ ¬Leal(Marco,Cesar)
7. IntentaAsesinar(Marco,Cesar)

Odia(Marco,Cesar)?
'''

ejemplo2 = {
    'clausulas': [
        'Hombre(Marco)',
        'Pompeyano(Marco)',
        '¬Pompeyano(Marco) ∨ Romano(Marco)',
        'Gobernante(Cesar)',
        '¬Romano(Marco) ∨ Leal(Marco,Cesar) ∨ Odia(Marco,Cesar)',
        '¬Hombre(Marco) ∨ ¬Gobernante(Cesar) ∨ ¬IntentaAsesinar(Marco,Cesar) ∨ ¬Leal(Marco,Cesar)',
        'IntentaAsesinar(Marco,Cesar)'
    ],
    'pregunta': 'Odia(Marco,Cesar)'
}

'''
1. ¬Niño(x1) ∨ Ama(x1,PapáNoel)
2. ¬Ama(x2,PapáNoel) ∨ ¬Reno(y2) ∨ Ama(x2,y2)
3. Reno(Rodolfo)
4. NarizRoja(Rodolfo)
5. ¬NarizRoja(x5) ∨ Raro(x5) ∨ Payaso(x5)
6. ¬Reno(x6) ∨ ¬Payaso(x6)
7. ¬Raro(x7) ∨ ¬Ama(Scrooge,x7)

¬Niño(Scrooge)?
'''

ejemplo3 = {
    'clausulas': [
        '¬Niño(x1) ∨ Ama(x1,PapáNoel)',
        '¬Ama(x2,PapáNoel) ∨ ¬Reno(y2) ∨ Ama(x2,y2)',
        'Reno(Rodolfo)',
        'NarizRoja(Rodolfo)',
        '¬NarizRoja(x5) ∨ Raro(x5) ∨ Payaso(x5)',
        '¬Reno(x6) ∨ ¬Payaso(x6)',
        '¬Raro(x7) ∨ ¬Ama(Scrooge,x7)'
    ],
    'pregunta': '¬Niño(Scrooge)'
}

'''
1. Hombre(Marco)
2. Pompeyano(Marco)
3. ¬Pompeyano(x3) ∨ Romano(x3)
4. Gobernante(Cesar)
5. ¬Romano(x5) ∨ Leal(x5,Cesar) ∨ Odia(x5,Cesar)
6. ¬Hombre(x6) ∨ ¬Gobernante(y6) ∨ ¬IntentaAsesinar(x6,y6) ∨ ¬Leal(x6,y6)
7. IntentaAsesinar(Marco,Cesar)

Odia(Marco,Cesar)?
'''

ejemplo4 = {
    'clausulas': [
        'Hombre(Marco)',
        'Pompeyano(Marco)',
        '¬Pompeyano(x3) ∨ Romano(x3)',
        'Gobernante(Cesar)',
        '¬Romano(x5) ∨ Leal(x5,Cesar) ∨ Odia(x5,Cesar)',
        '¬Hombre(x6) ∨ ¬Gobernante(y6) ∨ ¬IntentaAsesinar(x6,y6) ∨ ¬Leal(x6,y6)',
        'IntentaAsesinar(Marco,Cesar)'
    ],
    'pregunta': 'Odia(Marco,Cesar)'
}


'''
1. ¬Americano(x1) ∨ ¬Arma(y1) ∨ ¬Vende(x1,y1,z1) ∨ ¬Hostil(z1) ∨ Criminal(x1)
2. ¬Misil(x2) ∨ ¬Posee(Nono,x2) ∨ Vende(West,x2,Nono)
3. ¬Enemigo(x3,America) ∨ Hostil(x3)
4. ¬Misil(x4) ∨ Arma(x4)
5. Posee(Nono, M1)
6. Misil(M1)
7. Americano(West)
8. Enemigo(Nono,America)

Criminal(West)?
'''

ejemplo5 = {
    'clausulas': [
        '¬Americano(x1) ∨ ¬Arma(y1) ∨ ¬Vende(x1,y1,z1) ∨ ¬Hostil(z1) ∨ Criminal(x1)',
        '¬Misil(x2) ∨ ¬Posee(Nono,x2) ∨ Vende(West,x2,Nono)',
        '¬Enemigo(x3,America) ∨ Hostil(x3)',
        '¬Misil(x4) ∨ Arma(x4)',
        'Posee(Nono,M1)',
        'Misil(M1)',
        'Americano(West)',
        'Enemigo(Nono,America)'
    ],
    'pregunta': 'Criminal(West)'
}
