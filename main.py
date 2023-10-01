
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

from helpers.resolucion import inferencia_resolucion

def main() -> None:
    clausulas = [
        '¬Niño(Scrooge) ∨ Ama(Scrooge,PapáNoel)',
        '¬Ama(Scrooge,PapáNoel) ∨ ¬Reno(Rodolfo) ∨ Ama(Scrooge,Rodolfo)',
        'Reno(Rodolfo)',
        'NarizRoja(Rodolfo)',
        '¬NarizRoja(Rodolfo) ∨ Raro(Rodolfo) ∨ Payaso(Rodolfo)',
        '¬Reno(Rodolfo) ∨ ¬Payaso(Rodolfo)',
        '¬Raro(Rodolfo) ∨ ¬Ama(Scrooge,Rodolfo)'
    ]
    
    pregunta = '¬Niño(Scrooge)'

    print(inferencia_resolucion(clausulas, pregunta))

if __name__ == '__main__':
    main()
