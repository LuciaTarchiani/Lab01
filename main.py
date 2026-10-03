import operator
import random

from domanda import leggi_domande, leggi_punti, Giocatore

lista_domande = leggi_domande("domande.txt")

livello_max = 0;
for d in lista_domande:
    if ( d.estrai_livello()> livello_max ):
        livello_max = d.estrai_livello()

#SUDDIVIDO LE DOMANDE IN BASE AL LORO LIVELLO
# CREAO UNA LISTA DI LISTE --> ad ogni indice di posizione della lista corrisponde
#una lista contente le domande del livello pari all'indice.
# (es: in posizione 0 si troverà la lista delle domande aventi livello 0]

domande_per_livello = []
i = 0
while i <= livello_max:
    domande_per_livello.append([])
    i = i + 1

for d in lista_domande:
    domande_per_livello[d.estrai_livello()].append(d)

#INIZIO GIOCO
l=0
punteggio = 0
while l <= livello_max:
    domanda = random.choice(domande_per_livello[l])
    print(f"Livello {l}) : {domanda.testo}")
    #andiamo a prendere la lista delle risposte alla domanda e mescoliamo le risposte
    domande_shuffle = domanda.risposte()
    random.shuffle(domande_shuffle)
    n =1
    for r in domande_shuffle:
        print(f" {n}. {r}")
        n = n+1
    valore = int(input("La risposta giusta è: "))

    if domande_shuffle[valore-1].strip() != domanda.estarai_risposta_giusta():
        for r in range(0,len(domande_shuffle)):
            if (domande_shuffle[r] == domanda.estarai_risposta_giusta()):
                break
        risposta_giusta = r+1
        print(f"Risposta errata. La risposta giusta era {risposta_giusta}. \n")
        break

    print("Risposta giusta!\n")
    punteggio = punteggio + 1
    l = l+1

print(f"Hai totalizzato {punteggio} punti.")
nickname = input("inserisci il tuo nickname: ")

nuovo = Giocatore(nickname,punteggio)
lista_giocatori = leggi_punti("punti.txt")
lista_giocatori.append(nuovo)

#ordiniamo la lista di giocatori
lista_giocatori.sort(key=operator.itemgetter('punteggio'),reverse=True)

