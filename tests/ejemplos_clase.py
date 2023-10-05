

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
    'pregunta': '¬Odia(Marco,Cesar)'
}
