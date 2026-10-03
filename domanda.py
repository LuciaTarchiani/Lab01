from dataclasses import dataclass

@dataclass
class Domanda:
    testo:str
    difficolta:int
    giusta:str
    errata1:str
    errata2:str
    errata3:str

    def estrai_livello(self):
        return(self.difficolta)

    def risposte(self):
        return [self.giusta,self.errata1,self.errata2,self.errata3]

    def estarai_risposta_giusta(self):
        return self.giusta


@dataclass
class Giocatore:
    nickname: str
    punteggio: int


def leggi_domande(file):
    testo=[]
    with open(file,'r',encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            if riga :
                testo.append(riga)

    # andiamo a raggruppare le righe del testo per creare le domande
    lista_domande=[]
    i = 0
    while i+6 <= len(testo):
        d = Domanda(testo[i],int(testo[i+1]),testo[i+2],testo[i+3],testo[i+4],testo[i+5])
        lista_domande.append(d)
        i = i + 6

    return lista_domande

def leggi_punti(file):
    lista_giocatori = []
    with open(file,'r',encoding="utf-8") as f:
        for riga in f:
            campi = riga.split()
            nickname = campi[0]
            punteggio = int(campi[1])
            lista_giocatori.append(Giocatore(nickname,punteggio))

    return lista_giocatori


