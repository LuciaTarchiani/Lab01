from dataclasses import dataclass

@dataclass
class Domanda:
    testo:str
    difficolta:int
    giusta:str
    errata1:str
    errata2:str
    errata3:str



def leggi_domande(file):
    testo=[]
    with open(file,'r',encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            if riga :
                testo.append(riga.strip())

    # andiamo a raggruppare le righe del testo per creare le domande
    lista_domande=[]
    i = 0
    while i+6 <= len(testo):
        d = Domanda(testo[i],int(testo[i+1]),testo[i+2],testo[i+3],testo[i+4],testo[i+5])
        lista_domande.append(d)
        i = i + 6

    return lista_domande
